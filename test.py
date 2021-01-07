import pandas as pd
import numpy as np
import jinja2

df = pd.read_csv('data.csv', sep=";")


#print(list(df.count().keys())[1:])
#print(df.count().values.tolist()[1:])

# Freq distribution
#arr = pd.array(df['Black'],dtype=pd.Int64Dtype())
arr = df['Black'].values.tolist()

#s = pd.Series(arr, dtype='Int64')
#print(s)


#print("Raw data: ", arr, "Agg data: ", exc_int(arr))
s = df['Black'].str.split('\.').str[0]
df['Black'] = pd.to_numeric(s, errors='coerce').astype('Int64')
print(df['Black'].values)


# Count number freq
