import os
import yaml
from flask import Flask, redirect, url_for
from cooklang_handler import scan_directory,force_rescan


with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

recipe_directory = config['RECIPE_DIR']
recipe_cache_path = f"{config['CACHE']['ROOT']}/{config['CACHE']['ALL_RECIPES']}"

@app.route("/")
def home():
    all_recipes = scan_directory(recipe_directory,recipe_cache_path)
    return all_recipes

@app.route("/refresh-list")
def refresh_list():
    force_rescan(recipe_directory, recipe_cache_path)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
