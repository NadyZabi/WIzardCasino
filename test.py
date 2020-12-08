import pandas as pd
import numpy as np
import jinja2

df = pd.read_csv('data.csv', sep=";")
#print(df.head())

#name = 'Nadya'
#tm = jinja2.Template('Hellow {{ name }}')
#msg = tm.render(name=name)

#print(msg)

#for row in df.iterrows():
#    for cell in row:
#        msg = tm.render(name=cell)
#        print(msg)


#for row in df.iterrows():
    #print(row)
for index, row in df.iterrows():
    for cell in row:
        print(cell)
