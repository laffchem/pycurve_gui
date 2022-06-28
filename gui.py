from flaskwebgui import FlaskUI
from main import app

FlaskUI(app, width=800, height=800).run()