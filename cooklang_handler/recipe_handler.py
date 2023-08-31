import os
import json
import cooklang

from .recipe_subfunctions import retrieve_all

def force_rescan(directory, file_path):
    full_recipes = {'recipes': retrieve_all(directory)}
    with open(file_path, 'w') as recipe_cache:
        recipe_cache.write(json.dumps(full_recipes, indent=2))

def scan_directory(directory, file_path):
    if not os.path.isfile(file_path):
        force_rescan(directory, file_path)

    with open(file_path, 'r') as recipe_json:
        all_recipes = json.loads(recipe_json.read())
    return all_recipes






