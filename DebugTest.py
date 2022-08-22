from Cooklang.CookLangInterpreter import Recipe
from inspect import cleandoc

def printIngredients(recipe):
    for ingredient in recipe.ingredients:
        print(f"{ingredient.quantity.amount} {ingredient.quantity.unit} of {ingredient.name}")


entry = Recipe.parse("Recipes/TestRecipe.cook")
printIngredients(entry)

