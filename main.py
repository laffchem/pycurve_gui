from website import create_app
from flaskwebgui import FlaskUI

app = create_app()

ui = FlaskUI(app)

if __name__ == "__main__":
    # app.run()
    ui.run()

