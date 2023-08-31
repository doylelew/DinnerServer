from flask import Flask
from routes import recipe_routes, shopping_routes

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

app.register_blueprint(recipe_routes, url_prefix="/recipe-list")
app.register_blueprint(shopping_routes, url_prefix="/shopping-list")

if __name__ == "__main__":
    app.run(debug=True)
