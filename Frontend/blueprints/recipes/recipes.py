import sys
sys.path.append("..")

from flask import Blueprint, render_template, request, redirect, jsonify
import requests
from functions.verify_file import verify_filestorage

# Set up blueprint
recipes_bp = Blueprint("recipes", __name__, template_folder="templates")

# backend API base URL
base_api_url = "http://localhost:8170"

# Recipe Routes
@recipes_bp.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        if request.files:
            endpoint = f"{base_api_url}/upload_recipe"

            recipe_file = request.files["recipe"]
            verify_filestorage(recipe_file)

            recipe_text = recipe_file.stream
            response = requests.post(url=endpoint, data=recipe_text)


            recipe_file.close()
            if response.status_code == 200:
                return jsonify(response.json())
            else:
                print("Failed to contact Backend API")
                return redirect(request.url)
    
    else:      
        return render_template("Upload_recipe.html")
