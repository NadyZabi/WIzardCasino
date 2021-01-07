import pandas as pd
from typing import List


def column_to_int(df: pd.DataFrame, column: str) -> List:
    """
    Cast raw data in str format to integer
    :param df: raw input data frame read from csv file
    :param column: specific column in df to read the numbers from
    :return: List of numbers 
    """
    # column format should be in quotes
    try:
        s = df[column].str.split('\.').str[0]
        df[column] = pd.to_numeric(s, errors='coerce').astype('Int64')
        numbers = list(df[column].values.dropna())
    except AttributeError:
        df[column] = df[column].astype('Int64')
        numbers = list(df[column].values.dropna())
    return numbers


# TODO: use "full" function signature + docs
def count_frequency(my_list):
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    return freq
