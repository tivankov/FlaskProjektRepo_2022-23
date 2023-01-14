
from flask import Flask, render_template
app = Flask(__name__)

imestranice = "Gurman HR"
naslov = "Najukusnija jela"
copyright = "Gurman HR | 2022-2023"

@app.route("/")
def index():
    return render_template('index.html', imestranice = imestranice, naslov = naslov, copyright = copyright)

@app.route("/dogadaji")
def dogadaji():
    return render_template('dogadaji.html', imestranice = imestranice, naslov = naslov, copyright = copyright)

@app.route("/onama")
def onama():
    return render_template('about.html', imestranice = imestranice, naslov = naslov, copyright = copyright)

@app.route("/kontakt")
def kontakt():
    return render_template('kontakt.html', imestranice = imestranice, naslov = naslov, copyright = copyright)

@app.route("/placanje")
def placanje():
    return render_template('placanje.html', imestranice = imestranice, naslov = naslov, copyright = copyright)

@app.route("/placeno")
def placeno():
    return render_template('placeno.html', imestranice = imestranice, naslov = naslov, copyright = copyright)