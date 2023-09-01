from config import config
from flask import  Blueprint, redirect, url_for
from cooklang_handler import recipe_handler

recipe_routes = Blueprint("recipe_routes", __name__)

recipe_path = os.path.abspath(config['DIRECTORIES']['ROOT']['RECIPES']['PATH'])
data_cache_path =  os.path.abspath(config['DIRECTORIES']['ROOT']['DATA']['PATH'])
recipe_cache_path =  f"{data_cache_path}/{os.path.abspath(config['DIRECTORIES']['ROOT']['DATA']['RECIPES'])}"

@recipe_routes.route("/")
def recipe_list():
    all_recipes = recipe_handler.scan_directory(recipe_path, recipe_cache_path)
    return all_recipes

@recipe_routes.route("/refresh-list")
def refresh_list():
    recipe_handler.force_rescan(recipe_path, recipe_cache_path)
    return redirect(url_for('recipe_routes.recipe_list'))

@recipe_routes.route("/<int:index>")
def view_recipe(index):
    recipe_list = recipe_handler.scan_directory(recipe_path, recipe_cache_path)['recipes']
    recipe_object = recipe_handler.read_recipe(recipe_list, index)
    if not recipe_object:
        return { 'status': 404 ,'message':'recipe not found, try rescanning the directory'}, 404

    return recipe_object