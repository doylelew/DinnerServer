from Cooklang.CookLangInterpreter import Recipe
import itertools
import re
from dataclasses import dataclass
from fractions import Fraction
from typing import Mapping, Optional, Sequence, Tuple, Union


def printInfo(recipe):
    print("**********Metadata**********")
    for key in recipe.metadata:
        print(f"{key}: {recipe.metadata[key]}")

    print("**********Ingredients**********")
    for ingredient in recipe.ingredients:
        print(f"{ingredient.quantity.amount} {ingredient.quantity.unit} of {ingredient.name}")

    print("**********Steps**********")
    for step in recipe.steps:
        print(step)

filename = "Recipes/TestRecipe.cook"
entry = Recipe.parse(filename)

printInfo(entry)



