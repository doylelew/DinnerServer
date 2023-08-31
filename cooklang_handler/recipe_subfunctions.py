import re
import os

def find_images(directory, recipe_name):
    pattern = re.compile(rf"{recipe_name}(.?\d+)?.(?:jpg|jpeg|png)")
    image_list = [file for file in os.listdir(directory) if pattern.match(file)]
    return image_list

def retrieve_all(directory):
    recipe_list = []
    for item in os.listdir(directory):
        if item.endswith(".cook"):
            recipe_name = item.removesuffix(".cook")
            recipe_list.append(
                {'name': f'{recipe_name}',
                 'images': find_images(directory, recipe_name),
                 'category': directory}
            )

        if os.path.isdir(os.path.join(directory, item)):
            recipe_list.extend(retrieve_all(f"{directory}/{item}"))

    return recipe_list