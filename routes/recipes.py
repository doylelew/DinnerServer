import yaml
from flask import  Blueprint, redirect, url_for
from cooklang_handler import recipe_handler

recipe_routes = Blueprint("recipe_routes", __name__)

with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

recipe_directory = config['RECIPE_DIR']
recipe_cache_path = f"{config['CACHE']['ROOT']}/{config['CACHE']['ALL_RECIPES']}"

@recipe_routes.route("/")
def recipe_list():
    all_recipes = recipe_handler.scan_directory(recipe_directory,recipe_cache_path)
    return all_recipes

@recipe_routes.route("/refresh-list")
def refresh_list():
    recipe_handler.force_rescan(recipe_directory, recipe_cache_path)
    return redirect(url_for('recipe_routes.recipe_list'))

@recipe_routes.route("/recipe/<int:index>")
def view_recipe(index):
    recipe_list = recipe_handler.scan_directory(recipe_directory,recipe_cache_path)['recipes']
    recipe_object = recipe_handler.read_recipe(recipe_list, index)
    if not recipe_object:
        return { 'status': 404 ,'message':'recipe not found, try rescanning the directory'}, 404

    return recipe_object