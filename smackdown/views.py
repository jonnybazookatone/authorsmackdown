# encoding: utf-8
"""
Views
"""
import ads
from flask import current_app, request, abort
from flask.ext.restful import Resource
from utils import get_post_data

MINUTES = 60.0  # seconds
SYSTEMSGO_CACHE_TIMEOUT = 5*MINUTES

class IndexView(Resource):
    """
    Return the index page. This is temporary until the app is deployed on its
    own instance.
    """
    def get(self):
        """
        HTTP GET request
        :return: index html page
        """
        return current_app.send_static_file('index.html')

class SmackView(Resource):
    """
    End point for the smackdown
    """

    def post(self):
        """
        HTTP POST Request
        Return the statistics for two queries.
        """

        post_data = get_post_data(request)

        try:
            author1 = ads.SearchQuery(q=post_data['query1'], fl=['id', 'bibcode'])
            author2 = ads.SearchQuery(q=post_data['query2'], fl=['id', 'bibcode'])
        except KeyError:
            abort(404)

        bibcodes1 = [paper.bibcode for paper in author1]
        bibcodes2 = [paper.bibcode for paper in author2]

        riq1 = 0
        riq2 = 0

        if bibcodes1:
            metrics1 = ads.MetricsQuery(bibcodes=bibcodes1)
            response1 = metrics1.execute()
            riq1 = response1['indicators']['riq']

        if bibcodes2:
            metrics2 = ads.MetricsQuery(bibcodes=bibcodes2)
            response2 = metrics2.execute()
            riq2 = response2['indicators']['riq']

        response = {
            'author1': {
                'riq': riq1
            },
            'author2': {
                'riq': riq2
            }
        }

        return response, 200
