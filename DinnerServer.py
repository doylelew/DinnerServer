from flask import Flask

from routes.recipes import recipe_routes

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

app.register_blueprint(recipe_routes, url_prefix="/recipe-list")

if __name__ == "__main__":
    app.run(debug=True)
