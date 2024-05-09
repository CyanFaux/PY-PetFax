# took from Blackbox AI
from flask import Flask, render_template

app = Flask(__name__)

# Assume we have a database with pet information
pets = [
    {"name": "Fluffy", "species": "cat"},
    {"name": "Spot", "species": "dog"},
    {"name": "Tweety", "species": "bird"},
]

@app.route("/")
def index():
    return render_template("index.html", pets=pets)

@app.route("/pets/<int:pet_id>")
def show_pet(pet_id):
    pet = pets[pet_id]
    return render_template("show_pet.html", pet=pet)

if __name__ == "__main__":
    app.run()