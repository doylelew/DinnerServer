import os
import time
import yaml
import json
from flask import Flask, redirect, url_for
from cooklang_handler import recipe_handler


with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

recipe_directory = config['RECIPE_DIR']
recipe_cache_path = f"{config['CACHE']['ROOT']}/{config['CACHE']['ALL_RECIPES']}"

@app.route("/")
def home():
    if not os.path.isfile(recipe_cache_path):
        recipe_handler.scan_directory(recipe_directory, recipe_cache_path)
    with open(recipe_cache_path, 'r') as recipe_json:
        all_recipes = json.loads(recipe_json.read())
    return all_recipes

@app.route("/refresh-list")
def refresh_list():
    recipe_handler.scan_directory(recipe_directory, recipe_cache_path)
    return redirect(url_for('home'))
