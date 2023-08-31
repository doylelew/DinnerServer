import yaml
from flask import Flask
import yaml
from cooklang_handler import recipe_handler

with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/")
def home():

    all_recipes = recipe_handler.retrieve_all(config['RECIPE_DIR'])

    return all_recipes