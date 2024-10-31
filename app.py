from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'tajni_ključ'  # Ovo postavljamo kao tajni ključ za sigurnost
bootstrap = Bootstrap5(app)

class NameForm(FlaskForm):
    name = StringField("Ime", validators=[DataRequired()])
    submit = SubmitField("Pošalji")

@app.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():  # Provjerava li je obrazac uspješno poslan i validiran
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Promijenili ste ime!', 'success')
        session['name'] = form.name.data # pohranjuje ime u sesiju
        return redirect(url_for('index'))  # Preusmjeravamo na istu rutu 'index'
    return render_template('index.html', name = session.get('name'), form = form)