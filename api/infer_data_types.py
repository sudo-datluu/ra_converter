import pandas as pd
import numpy as np

# Return true if the column is numeric
def convert_to_numeric(df, col):
    df_converted = pd.to_numeric(df[col], errors='coerce')
    if not df_converted.isna().all():  # If at least one value is numeric
        df[col] = df_converted
        return True
    return False

# Try to convert to datetime
def convert_to_datetime(df, col):
    try:
        df[col] = pd.to_datetime(df[col])
        return True
    except (ValueError, TypeError):
        return False

# Try to convert to boolean
def convert_to_bool(df, col):
    unique_values = df[col].unique()
    if set(unique_values) == {0, 1} or set(unique_values) == {'True', 'False'} or set(unique_values) == {True, False}:
        df[col] = df[col].astype(bool)
        return True
    return False

# Try to convert to timedelta
def convert_to_timedelta(df, col):
    df_converted = pd.to_timedelta(df[col], errors='coerce')
    if not df_converted.isna().all():  # If at least one value is timedelta
        df[col] = df_converted
        return True
    return False

# convert to complex number
# assumes the complex number is in the form a+bi
def convert_to_complex(df, col):
    try:
        df[col] = df[col].apply(lambda x: complex(x.replace('i', 'j')))
        return True
    except ValueError:
        return False

# Convert to categorical column
def convert_to_categorical(df, col, categorical_threshold):
    if len(df[col].unique()) / len(df[col]) < categorical_threshold:  # Example threshold for categorization
        df[col] = pd.Categorical(df[col])
        return True
    return False

# get categorical threshold based on number of rows
def adjust_categorical_threshold(df):
    total_rows = len(df)
    if total_rows <= 10:
        return 0.5
    elif total_rows <= 100:
        return 0.3
    else:
        return 0.2

def infer_and_convert_data_types(df, categorical_threshold=0.5):
    categorical_threshold = adjust_categorical_threshold(df)
    for col in df.columns:
        if convert_to_numeric(df, col): continue
        if convert_to_datetime(df, col): continue
        if convert_to_bool(df, col): continue
        if convert_to_timedelta(df, col): continue
        if convert_to_complex(df, col): continue
        if convert_to_categorical(df, col, categorical_threshold): continue
    return df