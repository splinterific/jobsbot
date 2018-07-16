import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    VERIFICATION_TOKEN = os.environ.get(
        "JB_VERIFICATION_TOKEN")
    BOT_TOKEN = os.environ.get("JOB_BOT_TOKEN")
    USER_TOKEN = os.environ.get("JOB_USER_TOKEN")
    OAUTH_SCOPE = os.environ.get("SCOPES")
    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_SECRET = os.environ.get(
        "CLIENT_SECRET")