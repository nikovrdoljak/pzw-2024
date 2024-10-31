from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap5(app)

class NameForm(FlaskForm):
    name = StringField("Ime", validators=[DataRequired()])
    submit = SubmitField("Pošalji")

@app.route("/", methods=["GET", "POST"])
def index():
    name = ""
    if request.method == "POST":
        # Ako je POST, podatke dobijemo iz request.form
        name = request.form.get("name", "")
    else:
        # Ako je GET, podatke dobijemo iz request.args
        name = request.args.get("name", "") 
    return render_template("index.html", name = name) 