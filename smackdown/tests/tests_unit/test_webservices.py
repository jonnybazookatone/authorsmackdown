# coding: utf-8
"""
Test webservices
"""

import sys
import os
PROJECT_HOME = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(PROJECT_HOME)

import re
import app
import json
import unittest

from flask import url_for
from flask.ext.testing import TestCase
from stub_data import example_metrics_response
from mocks import MockSolrResponse, MockMetricsResponse


class TestSmackdown(TestCase):
    """
    A basic base class for all of the tests here
    """

    def create_app(self):
        """
        Create the wsgi application
        """
        app_ = app.create_app()
        return app_

    def test_that_smackview_returns_json_on_post(self):
        """
        Tests that the SmackView returns a JSON string with the
        expected format
        """
        url = url_for('smackview')
        data = {'query1': 'test', 'query2': 'test'}

        with MockSolrResponse(api_endpoint=re.compile('.*search.*')) as SR, \
                MockMetricsResponse(api_endpoint=re.compile('.*metrics.*')) as MR:
            response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, 200)

        expected_json = {'author1': {'riq': json.loads(example_metrics_response)['indicators']['riq']},
                         'author2': {'riq': json.loads(example_metrics_response)['indicators']['riq']}}

        actual_json = response.json

        self.assertEqual(
            expected_json['author1']['riq'],
            actual_json['author1']['riq']
        )
        self.assertEqual(
            expected_json['author2']['riq'],
            actual_json['author2']['riq']
        )

    def test_root_returns_index(self):
        """
        Tests that the root path returns the index html. This is a temporary
        hack for testing simply.
        """
        url = url_for('indexview')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main(verbosity=2)
