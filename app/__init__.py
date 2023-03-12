from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap4 
from app.middleware import PrefixMiddleware

application = Flask(__name__)
application.config.from_object(Config)
bootstrap = Bootstrap4(application)

# set voc=False if you run on local computer
application.wsgi_app = PrefixMiddleware(application.wsgi_app, voc=False)


from app import routes
