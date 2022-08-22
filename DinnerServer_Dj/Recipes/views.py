from django.shortcuts import render
from django.http import HttpResponse

# Home Page View
def home(request):
    return HttpResponse("<h1>Home Page!!!!!</h1>")

def about(request):
    return HttpResponse("<h2>Here is how you use this cool site</h2>")
