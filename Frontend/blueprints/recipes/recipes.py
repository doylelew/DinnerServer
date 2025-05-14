from flask import Blueprint, render_template, request, redirect, jsonify
import requests

recipes_bp = Blueprint("recipes", __name__, template_folder="templates")

base_api_url = "http://localhost:8170"

@recipes_bp.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        if request.files:
            recipe_file = request.files["recipe"]

            endpoint = f"{base_api_url}/upload_recipe"

            recipe_text = recipe_file.stream
            response = requests.post(url=endpoint, data=recipe_text)


            recipe_file.close()
            if response.status_code == 200:
                return jsonify(response.json())
            else:
                print("Failed to contact Backend API")
                return redirect(request.url)

            
            
            
        

    return render_template("Upload_recipe.html")
