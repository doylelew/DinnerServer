import yaml
from flask import Blueprint

shopping_routes = Blueprint("shopping_routes", __name__)

with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

recipe_directory = config['RECIPE_DIR']
recipe_cache_path = f"{config['CACHE']['ROOT']}/{config['CACHE']['ALL_RECIPES']}"


@shopping_routes.route("/")
def shopping_list():
    return "One day the things you need to shop for whill show up here"
