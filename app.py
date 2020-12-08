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
"""
data = pd.read_csv("data.csv", sep=',', header=None, index_col=False)

#for row in data.iterrows():
#    print(row)

print(data)
"""
data = (
    ('00:38:25','','0',''),
    ('00:37:38','15','',''),
    ('00:36:48','','','32'),
    ('00:35:56','','','18'),
    ('00:34:27','','','7')
)

@app.route('/table')
def table():
    return render_template("table.html", headings=headings, data=data)

if __name__=="__main__":
    app.run(debug=True)
