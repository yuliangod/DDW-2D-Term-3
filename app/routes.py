from app import application
from flask import render_template, flash, redirect, url_for
from app.forms import CreateQuestionForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from flask import request 
from app.serverlibrary import * 
import pandas as pd

# function to create json string from python dataframe
def create_json(predictor_name):
    df = pd.read_csv("DDW 2D Dataset.csv")
    df2 = pd.DataFrame()
    df2["x"] = df[predictor_name]
    df2["y"] = df["Crop Yield"]
    df2 = df2.to_json(orient = 'records')
    return df2

@application.route("/", methods=('GET', 'POST'))
@application.route("/index", methods=('GET', 'POST'))
def index():
    form = CreateQuestionForm()
    pred = "__"
    if form.validate_on_submit():
        temperature = float(form.temperature.data)
        precipitation = float(form.precipitation.data)
        methane = float(form.methane.data)
        nitrous_oxide = float(form.nitrous_oxide.data)

        pred = -37201.01142 + 61.36965642*methane + 47.00918803*nitrous_oxide + -103.4736757*precipitation + 311.0397424*temperature
        print(pred)
    return render_template("index.html", form=form, pred= pred)

@application.route("/info")
def info():
    B0 = -37201.01142
    B1 = 61.36965642
    B2 = 47.00918803
    B3 = -103.4736757
    B4 = 311.0397424
    return render_template("info.html", B0=B0, B1=B1, B2=B2, B3=B3, B4=B4)

@application.route("/methane")
def methane():
    data = create_json("Methane (million metric tons of carbon dioxide equivalent)")
    return render_template("graph.html", data=data, name="Methane")

@application.route("/nitrous_oxide")
def nitrous_oxide():
    data = create_json("Nitrous oxide (million metric tons of carbon dioxide equivalent)")
    return render_template("graph.html", data=data, name="Nitrous Oxide")

@application.route("/temperature")
def temperature():
    data = create_json("Average Annual Temperature(F)")
    return render_template("graph.html", data=data, name="Temperature")

@application.route("/precipitation")
def precipitation():
    data = create_json("Annual Precipitation Value(mm)")
    return render_template("graph.html", data=data, name="Precipitation")




