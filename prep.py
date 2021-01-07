import pandas as pd

def col_to_int(df,col):
    # col format should be in quotes
    try:
        s = df[col].str.split('\.').str[0]
        df[col] = pd.to_numeric(s, errors='coerce').astype('Int64')
        num = list(df[col].values.dropna())
    except AttributeError:
        df[col] = df[col].astype('Int64')
        num = list(df[col].values.dropna())
    return(num)


def CountFrequency(my_list):
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    return(freq)
