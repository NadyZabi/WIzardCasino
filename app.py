from flask import Flask, render_template, url_for, request
import pandas as pd
import numpy as np
from raw_data_preparation import column_to_int, count_frequency
from typing import Any

app = Flask(__name__)
# Table parametres
# should go to models.py
headings = ('Time','Black','Zero','Red')
data = pd.read_csv('data.csv', sep=";")
cat = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5,
       24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]

red_cat = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34 ,36]
black_cat =[2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33 , 35]
zero_cat=[0]

# models.py - M in MVC

tmp = pd.read_csv('data.csv', sep=";")

def read_again(file_name: str = "data.csv"):
    """ read the content of the file """
    return pd.read_csv(file_name, sep=";")

# end of model py



# should be in controller.py:
#def render_index() -> Any:
#    """ prepare data for user view """
#    return render_template("index.html")

def get_stats(refresh: str, colors):
    """
    Get stats and refresh data source if needed
    :param refresh: bool if the source of data should be read again for this request
    :return: render_template function with all params
    """
    # from models.py import tmp
    tmp = data
    if refresh=="1":
        print("Yassss!")
        tmp = read_again()

    num =[]
    for color in colors:

        arr = column_to_int(tmp,color)
        num +=arr
        miss_key = (set(cat) - set(count_frequency(num).keys()))
        miss_val = { i : 0 for i in miss_key }

        labels = list(count_frequency(num).keys())+list(miss_key)
        val = list(count_frequency(num).values())+list(miss_val.values())


    return headings, tmp, labels, val


@app.route('/')
def index():
    return render_template("index.html")


# Visual endpoint
@app.route('/about')
def about():
    return render_template("about.html")


# TODO: an example of an API endpoint not returning "Visual" result
@app.route('/give_data')
def return_data():
    # !REMEMBER! return statement in this approach NEEDS to be json serializable a.k.a. dict-like
    return str(column_to_int(data, "Red"))


@app.route('/stat')
def stat():
    """
    Show nice statistics from some source

    :Query params: refresh - if 1 read new source, else use old one
    """
    #MyChart
    # tmp = pd.read_csv('data.csv', sep=";")
    # #val = tmp.count().values.tolist()[1:]
    # #labels = list(tmp.count().keys())[1:]
    # num = []
    # for col in headings[1:]:
    #     arr = column_to_int(tmp,col)
    #     num +=arr
    #
    # miss_key = (set(cat) - set(count_frequency(num).keys()))
    # miss_val = { i : 0 for i in miss_key }
    #
    # labels = list(count_frequency(num).keys())+list(miss_key)
    # val = list(count_frequency(num).values())+list(miss_val.values())
    #
    # return render_template("stat.html",headings=headings, data=tmp,labels=labels, val=val)
    params = request.args.to_dict(flat=False)
    refresh = '0' if "refresh" not in params.keys() else params["refresh"]
    colors = ['Red', 'Black', 'Zero'] if "color" not in params.keys() else params["color"]
    print(colors)
    headings, data, labels, val = get_stats(refresh, colors)
    return render_template("stat.html", headings=headings, data=data, labels=labels, val=val)

if __name__=="__main__":
    app.run(debug=True)
