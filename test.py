import pandas as pd
import numpy as np
import jinja2
from prep import col_to_int, CountFrequency


df = pd.read_csv('data.csv', sep=";")
cols = ['Black','Zero','Red']

#print(list(df.count().keys())[1:])
#print(df.count().values.tolist()[1:])

# Freq distribution
num = []
for col in cols:
    arr = col_to_int(df,col)
    num +=arr

cat = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5,
       24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
miss_key = (set(cat) - set(CountFrequency(num).keys()))
miss_val = { i : 0 for i in miss_key }


print(list(CountFrequency(num).keys())+list(miss_key))
print(list(CountFrequency(num).values())+list(miss_val.values()))
