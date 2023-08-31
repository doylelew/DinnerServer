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

def read_recipe(recipe_list, index):
    if index not in range(len(recipe_list)):
        return None
    recipe_path = f"{recipe_list[index]['category']}/{recipe_list[index]['name']}.cook"
    if not os.path.isfile(recipe_path):
        return None

    recipe_object = cooklang.parseRecipe(recipe_path)
    recipe_object['metadata']['DinnerServer'] = recipe_list[index]
    recipe_object['metadata']['DinnerServer']['index'] = index

    return recipe_object






