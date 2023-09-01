import yaml
import os

with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

BASE_PATH = os.path.abspath(__file__).replace("\\",'/').removesuffix("/config.py")

def findKey(object, target_key):
    output = []
    for key in object:
        if not key == target_key:
            if type(object[key]) == str:
                continue
            found = findKey(object[key], target_key)
            if not found:
                continue
            output.append(key)
            output.extend(found)
            return output
        output.append(key)
    return output


def construct_path(KEY):
    path_tree = findKey(config['DIRECTORIES'], KEY)
    path = BASE_PATH
    state = config['DIRECTORIES']

    for key in path_tree:
        state = state[key]
        path = f"{path}/{state['NAME']}"

    return path




