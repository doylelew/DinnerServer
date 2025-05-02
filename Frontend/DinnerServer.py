from flask import Flask
from views import views
import json

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

app.register_blueprint(views, url_prefix="/")


if __name__ == "__main__":
    app.run(debug=True)
