import os
import cooklang

def retrieve_all(directory):
    recipe_list = []
    for item in os.listdir(directory):
        if item.endswith(".cook"):
            recipe_list.append({'name': f'{item.removesuffix(".cook") }', 'images': [], 'category': directory})

    return recipe_list
