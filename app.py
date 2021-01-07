from flask import Flask, render_template, url_for
import pandas as pd
import numpy as np
from prep import col_to_int, CountFrequency


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
cat = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5,
       24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]

@app.route('/stat')
def stat():
    #MyChart
    tmp = pd.read_csv('data.csv', sep=";")
    #val = tmp.count().values.tolist()[1:]
    #labels = list(tmp.count().keys())[1:]
    num = []
    for col in headings[1:]:
        arr = col_to_int(tmp,col)
        num +=arr

    miss_key = (set(cat) - set(CountFrequency(num).keys()))
    miss_val = { i : 0 for i in miss_key }

    labels = list(CountFrequency(num).keys())+list(miss_key)
    val = list(CountFrequency(num).values())+list(miss_val.values())

    return render_template("stat.html",headings=headings, data=tmp,labels=labels, val=val)

if __name__=="__main__":
    app.run(debug=True)
