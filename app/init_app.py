# Import flask and template operators
from flask import Flask
# Import script
from flask_script import Manager
# Import CsrfProtect
from flask_wtf.csrf import CSRFProtect
# Import Bootstrap
from flask_bootstrap import Bootstrap

app = Flask(__name__)  # The WSGI compliant web application object

# Read common settings from 'config.py'
app.config.from_object('config')

# Read environment-specific settings from 'local_config.py'
try:
    app.config.from_object('local_config')
except ImportError:
    print("The configuration file 'local_config.py' does not exist.\n" +
            "Please copy local_config_example.py to local_config.py\n" +
            "and customize its settings before you continue.")
    exit()

if app.testing:
    app.config[
        'WTF_CSRF_ENABLED'] = False  # Disable CSRF checks while testing

manager = Manager(app)  # Setup Flask-Script


# Initialize Flask Application
def init_app(app, extra_config_settings={}):

    # bootstrap app
    Bootstrap(app)
    # csrf protect app
    CSRFProtect(app)

    # Import app.views
    from app.views import home_page, page_not_found

