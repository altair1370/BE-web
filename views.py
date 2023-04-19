from flask import Flask, render_template
app = Flask(__name__)
#app.template_folder = "template"
#app.static_folder = "static"
app.config.from_object('myApp.config')
@app.route("/")
def index():
    return render_template("index.html")
# page autentification 
@app.route("/login")
def login():
    return render_template("login.html")

#deconnexion
@app.route("/logout")
def logout():
    return redirect('/login')

#rappels SGBD
@app.route("/sgbd")
def membres():
    return render_template("sgbd.html")

#gestion des fichiers
@app.route("/fichiers")
def fichiers():
    return render_template("fichiers.html")