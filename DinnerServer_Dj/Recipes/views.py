from django.shortcuts import render
from django.http import HttpResponse

recipe_list = [
    {
        'Title': 'Yummy Pad Thai',
        'Description': 'This is a dish, like revenge, best served cold',
        'Rating': 5,
    },
    {
        'Title': 'Eggs Benedict',
        'Description': 'serve your eggs like the cumberbatch kid',
        'Rating': 3.5,
    },
    {
        'Title': 'French Toast',
        'Description': 'Be like the french and eat all the fats',
        'Rating': 5,
    },

]

# Home Page View
def home(request):
    context = {
        'recipes' :recipe_list,
        'title':"home",
               }
    return render(request, "Recipes/home.html", context = context)

def about(request):
    return render(request, "Recipes/about.html", context={'title': "about",})
