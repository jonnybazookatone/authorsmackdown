# encoding: utf-8
"""
Configuration file. Please prefix application specific config values with
the application name.
"""

# import os

# CORS
CORS_ORIGINS = ['https://authorsmackdown.herokuapp.com', 'http://authorsmackdown.herokuapp.com']

# Cache settings
CACHE = {
    'CACHE_TYPE': 'simple'
    # 'CACHE_TYPE': 'memcached',
    # 'CACHE_MEMCACHED': os.environ.get('MEMCACHIER_SERVERS', '').split(','),
    # 'CACHE_MEMCACHED_USERNAME': os.environ.get('MEMCACHIER_USERNAME', ''),
    # 'CACHE_MEMCACHED_PASSWORD': os.environ.get('MEMCACHIER_PASSWORD', '')
}
SMACKDOWN_CACHE_TIMEOUT = 10  # seconds

# Log settings
SMACKDOWN_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s\t%(process)d '
                      '[%(asctime)s]:\t%(message)s',
            'datefmt': '%m/%d/%Y %H:%M:%S',
        }
    },
    'handlers': {
        'file': {
            'formatter': 'default',
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '/tmp/smackdown.log',
        },
        'console': {
            'formatter': 'default',
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        '': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
