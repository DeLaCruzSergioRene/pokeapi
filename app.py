from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "héroe_del_escudo_temporada_1_god"
API = "https://pokeapi.co/api/v2/pokemon/"

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search_pokemon():
    pokemon_name = request.form.get("pokemon_name", "")
    
    if not pokemon_name:
        flash("Por favor ingresa un nombre")
        return redirect(url_for("index"))
    
try:
    resp = requests.get(f"{API}{pokemon_name}")
    if resp.status_code == 200:
        pokemon_data = resp-json()
        return render_template("pokemon.html")
    
if __name__ == "__main__":
    app.run(debug=True)