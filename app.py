from flask import Flask, render_template
import pandas as pd
from forms import CreateQuestionForm
import os
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

bootstrap = Bootstrap5(app)

# function to create json string from python dataframe
def create_json(predictor_name):
    df = pd.read_csv("DDW 2D Dataset.csv")
    df2 = pd.DataFrame()
    df2["x"] = df[predictor_name]
    df2["y"] = df["Crop Yield"]
    df2 = df2.to_json(orient = 'records')
    return df2

@app.route("/", methods=('GET', 'POST'))
@app.route("/index", methods=('GET', 'POST'))
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

@app.route("/info")
def info():
    B0 = -37201.01142
    B1 = 61.36965642
    B2 = 47.00918803
    B3 = -103.4736757
    B4 = 311.0397424
    return render_template("info.html", B0=B0, B1=B1, B2=B2, B3=B3, B4=B4)

@app.route("/methane")
def methane():
    data = create_json("Methane (million metric tons of carbon dioxide equivalent)")
    return render_template("graph.html", data=data, name="Methane")

@app.route("/nitrous_oxide")
def nitrous_oxide():
    data = create_json("Nitrous oxide (million metric tons of carbon dioxide equivalent)")
    return render_template("graph.html", data=data, name="Nitrous Oxide")

@app.route("/temperature")
def temperature():
    data = create_json("Average Annual Temperature(F)")
    return render_template("graph.html", data=data, name="Temperature")

@app.route("/precipitation")
def precipitation():
    data = create_json("Annual Precipitation Value(mm)")
    return render_template("graph.html", data=data, name="Precipitation")


