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

# Table parametres
headings = ('Time','Black','Zero','Red')
data = pd.read_csv('data.csv', sep=";")

@app.route('/stat')
def stat():
    tmp = pd.read_csv('data.csv', sep=";")
    val = tmp.count().values.tolist()[1:]
    labels = list(tmp.count().keys())[1:]
    return render_template("stat.html",headings=headings, data=data,labels=labels, val=val)

if __name__=="__main__":
    app.run(debug=True)
