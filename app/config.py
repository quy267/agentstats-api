# -*- coding: utf-8 -*-
import os


def make_dir(dir_path):
    try:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
    except Exception as e:
        raise e


class DefaultConfig(object):
    DEBUG = True
    FILENAME = __file__

    # Security
    # This is the secret key that is used for session signing.
    SECRET_KEY = os.urandom(24)

    # The filename for the info and error logs. The logfiles are stored at log-api/logs
    INFO_LOG = "info.log"
    ERROR_LOG = "error.log"
    current_path = os.path.dirname(__file__)
    LOG_FOLDER = os.path.join(os.path.abspath(os.path.dirname(current_path)), 'logs')

    IAM_HOST = '192.168.3.38'
    IAM_PORT = 8881

    OAUTH2_ENABLED = False
    OAUTH2_SERVER = '192.168.3.38'
    OAUTH2_PORT = 8881
    OAUTH2_CONSUMER_KEY = 'override me'
    OAUTH2_CONSUMER_SECRET = 'override me'

    # UDP Error reporting
    LOGSTASH_UDP_HOST = '192.168.3.22'
    LOGSTASH_UDP_PORT = 2514

    # MONGO DB Config
    # MONGO_HOST = '192.168.3.35'  # '$MONGODB_SERVER_IP'
    MONGO_HOST = 'localhost'  # '$MONGODB_SERVER_IP'
    MONGO_PORT = 27017  # '$PORT': mặc định là 27017
    # MONGO_PORT = 37017  # '$PORT': mặc định là 27017
    MONGO_DBNAME = 'agentstats'  # $MONGODB_NAME'
    # MONGO_USERNAME = 'agentstats'  # '$USERNAME'
    # MONGO_PASSWORD = '098poiA#'  # '$PASSWORD'


class AgentStatsAPIConfig(DefaultConfig):
    """Special config for AgentStats API"""
    pass