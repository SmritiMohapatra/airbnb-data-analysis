# @Author: smritimohapatra
# @Date:   2018-11-20T13:05:20+05:30
# @Last modified by:   smritimohapatra
# @Last modified time: 2018-12-11T09:17:09+05:30



"""
This helper module contains helper functions for wrangling the data
associated with the accompanied analysis notebook
"""
import pandas as pd
import numpy as np


def parse_df_dates(col):
    """
    Parse col of a dataframe to convert to datetime type

    Parameters:
    col
        Column of dataframe to be converted

    Returns:
    col
        Converted column
    """
    if col.dtypes == object:
        col = pd.to_datetime(col, errors='ignore')
    return col


def get_missing_percentage(series):
    """
    Get a list of columns with the percentage of missing data

    Parameters:
    series: dataframe
        Dataframe to be assessed for missing values

    Returns:
    series
        dataframe with missing percentage for all columns
    """
    return round(series.isnull().mean(), 4)


def get_missing_percentage_sorted(series):
    """
    Get a sorted list of columns with the percentage of missing data

    Parameters:
    series: dataframe
        Dataframe to be assessed for missing values

    Returns:
    series
        dataframe with missing percentage for all columns in a sorted manner
    """
    return get_missing_percentage(series).sort_values()

def get_redundant_cols(dataframe):
    """
    Get a list of redundant columns in a dataframe - columns that have the same value for all rows

    Parameters:
    df: Dataframe
        Dataframe to be assessed

    Returns:
    red_cols:
        List of redundant columns
    """
    #cols = list(df)
    nunique = dataframe.apply(pd.Series.nunique)
    red_cols = nunique[nunique == 1].index
    return red_cols
