from flask import Flask
from views import views
from blueprints.recipes.recipes import recipes_bp
import json

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

app.register_blueprint(views, url_prefix="/")
app.register_blueprint(recipes_bp, url_prefix="/recipes" )

if __name__ == "__main__":
    app.run(debug=True)