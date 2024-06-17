import csv
import os

from flask import Flask, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField
from wtforms.validators import DataRequired


app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = SECRET_KEY


class MyForm(FlaskForm):
    name = StringField("Name:", validators=[DataRequired()])
    email = EmailField("Email:", validators=[DataRequired()])
    feedback = TextAreaField("Feedback:", validators=[DataRequired()])


def write_to_csv(name, email, feedback):
    # Check to see if file exists
    try:
        with open("survey_results.csv", "r") as csvfile:
            empty = False
    except FileNotFoundError:
        empty = True
    with open("survey_results.csv", "a") as csvfile:
        cvswriter = csv.writer(csvfile)
        # Add headers to blank file
        if empty:
            cvswriter.writerow(["name", "email", "feedback"])
        # Add data from form
        cvswriter.writerow([name, email, feedback])


@app.route("/", methods=["GET", "POST"])
def home():
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        feedback = form.feedback.data
        write_to_csv(name, email, feedback)
        return redirect("/thank_you")
    return render_template("index.html", form=form)


@app.route("/thank_you", methods=["GET"])
def thank_you():
    return render_template("thank_you.html")


if __name__ == "__main__":
    app.run()
