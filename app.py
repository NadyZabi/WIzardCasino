from flask import Flask, render_template, url_for
import pandas as pd
import numpy as np


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/chart')
def chart():
    return render_template("chart.html")

# Table parametres

headings = ('Time','Black','Zero','Red')
data = pd.read_csv('data.csv', sep=";")

@app.route('/table')
def table():
    return render_template("table.html", headings=headings, data=data)

if __name__=="__main__":
    app.run(debug=True)
