# Import required packages
from numpy.core.fromnumeric import shape
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Read data into dataframes

june_2020_df = pd.read_csv("./data/202006-divvy-tripdata.csv")
july_2020_df = pd.read_csv("./data/202007-divvy-tripdata.csv")
august_2020_df = pd.read_csv("./data/202008-divvy-tripdata.csv")
september_2020_df = pd.read_csv("./data/202009-divvy-tripdata.csv")
october_2020_df = pd.read_csv("./data/202010-divvy-tripdata.csv")
november_2020_df = pd.read_csv("./data/202011-divvy-tripdata.csv")
december_2020_df = pd.read_csv("./data/202012-divvy-tripdata.csv")
january_2021_df = pd.read_csv("./data/202101-divvy-tripdata.csv")
february_2021_df = pd.read_csv("./data/202102-divvy-tripdata.csv")
march_2021_df = pd.read_csv("./data/202103-divvy-tripdata.csv")
april_2021_df = pd.read_csv("./data/202104-divvy-tripdata.csv")
may_2021_df = pd.read_csv("./data/202105-divvy-tripdata.csv")

# Create a list of all dataframes

frames = [
    june_2020_df,
    july_2020_df,
    august_2020_df,
    september_2020_df,
    october_2020_df,
    november_2020_df,
    december_2020_df,
    january_2021_df,
    february_2021_df,
    march_2021_df,
    april_2021_df,
    may_2021_df,
]

# Check number of columns for all the dataframes
# This step is necessary as it informs whether and how the dataframes can be joined
num_cols = []


def verify_num_of_cols(frames):
    for frame in frames:
        num_cols.append(len(frame.columns))
    return num_cols


# print(verify_num_of_cols(frames=frames))
# Here, we establish that each dataframe has 13 columns
# By inspecting the columns manually, we discover that they are appropriately named
# across the dataframes

# Create a single dataframe that combines the 12 dataframes
df = pd.concat(frames, axis=0, ignore_index=True)
print(df.columns)

# Summary of the data
print(df.head(10))
print(df.info())

# Data cleaning

# First we need to establish which columns and rows have missing data
# Columns with missing values
print(df.isnull().sum())

# Rows missing values
print(df[df.isnull().any(axis=1)])

# Examine the first row with missing values further
print(df.iloc[800])

# Find out the total number of rows that contain null values
sum_of_rows_with_null_values = df.isnull().any(axis=1).sum()
print(f"Total Null rows: {sum_of_rows_with_null_values}")

# Percentage of rows with missing values in the dataset
pc_nan_rows = sum_of_rows_with_null_values / df.shape[0] * 100
print(f"PC of null rows: {pc_nan_rows}")

# Drow rows with missing data
# Since rows with missing data appear to contain more than one missing value and
# only account for 7.7% of the dataset, we drop them.

clean_df = df.dropna(axis="index")

# Check if new df has any missing values
print(clean_df.isnull().sum())

# Summary of the clean df
print(clean_df)
