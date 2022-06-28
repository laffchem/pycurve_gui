from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config['UPLOAD_FOLDER'] = "uploads"
    app.config['ALLOWED_EXTENSIONS'] = {'csv'}

    from .views import views
    from .curves import curves

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(curves, url_prefix='/')

    return app