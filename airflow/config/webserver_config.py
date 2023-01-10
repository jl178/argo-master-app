import os
from flask_appbuilder.security.manager import AUTH_OAUTH
from airflow.configuration import conf
basedir = os.path.abspath(os.path.dirname(__file__))
AUTH_TYPE = AUTH_OAUTH
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = "Admin"
WTF_CSRF_ENABLED = True
CSRF_ENABLED = True
SQLALCHEMY_DATABASE_URI = conf.get("core", "SQL_ALCHEMY_CONN")
OAUTH_PROVIDERS = [
    {"name": "google", "icon": "fa-google", "token_key": "access_token",
    "remote_app": {
        "client_id": os.environ["GOOGLE_CLIENT_ID"],
        "client_secret": os.environ["GOOGLE_CLIENT_SECRET"],
        "api_base_url": "https://www.googleapis.com/oauth2/v2/",
        "client_kwargs": {
            "scope": "email profile"
        },
        "request_token_url": None,
        "access_token_url": "https://accounts.google.com/o/oauth2/token",
        "authorize_url": "https://accounts.google.com/o/oauth2/auth"}
    },
]