from flask import Flask
import os
PROJ_STATUS = "prod"
ALLOWED_EXTENSIONS = {'csv'}

def create_app():
    app = Flask(__name__)

    app.config['UPLOAD_FOLDER'] = "uploads"
    app.config['MAX_CONTENT_LENGTH'] = 5 * 1000 * 1000
    app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
    if PROJ_STATUS == "dev":
        app.config['SECRET_KEY'] ="secret"
        app.debug = True
    else:
        app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
        app.debug = False

    from .views import views
    from .models import models

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(models, url_prefix='/')

    return app