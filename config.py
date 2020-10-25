"""Flask configuration variables."""
from os import environ, path, getenv
from dotenv import load_dotenv

# Load environment variables from file .env, stored in this directory.
load_dotenv()

class Config:
    """Set Flask configuration from .env file."""

    # Flask configuration
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')
    SECRET_KEY = environ.get('SECRET_KEY')

    # Flask variables
    # ---------------
    FLASK_APP = 'wsgi.py'
    FLASK_ENV = 'development'  # 'development' or 'production'
    SECRET_KEY = '+Fus{=8MSV99y2ahF:@gcjtB_&J7f?}g'  # Used to encrypt session data.
    TESTING = False  # True or False.

    # WTForm variables
    # ----------------
    WTF_CSRF_SECRET_KEY = '$=H}j62u&SyJCy,JGELHx&3$jr6`>T3Y'  # Needed by Flask WTForms to combat cross-site request forgery.




