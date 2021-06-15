# Import required packages
from numpy.core.fromnumeric import shape, sort
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import datetime

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

# DATA CLEANING

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

# Drop rows with missing data
# Since rows with missing data appear to contain more than one missing value and
# only account for 7.7% of the dataset, we drop them.
# We do not drop the columns because they have less than 5% missing values

clean_df = df.dropna(axis="index")

# Check if new df has any missing values
# This step confirms that the data has no missing values
print(clean_df.isnull().sum())
print(clean_df)


# PROCESS DATA

# transform started_at and ended_at into datetime

clean_df["started_at"] = pd.to_datetime(clean_df["started_at"])
clean_df["ended_at"] = pd.to_datetime(clean_df["ended_at"])

print(clean_df.info())

# Sort dataframe in descending order based on ended_at colum
clean_df.sort_values(by=["ended_at"], inplace=True, ascending=False)
print(clean_df)

# From above, we notice that the dataframe contains some data for June 2021.
# Below we remove june 2021 data so that months = 12

june_2021_filter = df["ended_at"] <= "2021-06-03 00:00:00"
clean_df = clean_df[june_2021_filter]

# Create ride_length column (ride_length is in minutes)
ride_length = clean_df["ended_at"] - clean_df["started_at"]
ride_length = np.round(ride_length.dt.total_seconds() / 60, 2)
clean_df["ride_length"] = ride_length

# day_of_week
# This colum will contain the day of the week a ride started
clean_df["day_of_week"] = clean_df["started_at"].dt.day_name()

# month column
# clean_df["month"] = clean_df["started_at"].dt.strftime("%b")
clean_df["month"] = pd.DatetimeIndex(clean_df["started_at"]).month
print(clean_df)

# Get a summary of the data
data_descrption = clean_df.describe()
print(data_descrption)

# From this summary:
# We note that there are some negative values  for ride length
# Below we take a better look at them

print(clean_df[clean_df["ride_length"] < 0])

# 10k rows have negative values - we filter them out
clean_df = clean_df[clean_df["ride_length"] > 0]

# ANALYZE DATA

# Summary
data_descrption = clean_df.describe()
print(data_descrption)

# From the new summary:
# The average ride_length is 26.98 minutes
# The minimum ride length is 1.2 seconds
# The maximum ride length is 904.72hours, approxiamately 38days

# Find out what day of the week has the most bike hires

ride_hires_per_day = (
    clean_df["day_of_week"]
    .value_counts()
    .rename_axis("Day")
    .reset_index(name="Total Hires")
)
ride_hires_per_day.sort_values(by=["Total Hires"], inplace=True, ascending=True)
print(ride_hires_per_day)

plt.figure(figsize=(11, 5), dpi=100)
plt.title("Total Bike Hires per Day of the Week", loc="left", pad=20)
sns.barplot(data=ride_hires_per_day, x="Day", y="Total Hires")
plt.show()

# Find out how bike hires were distibuted throughout the year

ride_hires_per_month = (
    clean_df["month"]
    .value_counts(sort=False)
    .rename_axis("Month")
    .reset_index(name="Total Hires")
)
# ride_hires_per_month.sort_values(by=["Total Hires"], inplace=True, ascending=True)
months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]
print(ride_hires_per_month)

plt.figure(figsize=(11, 5), dpi=100)
plt.title("Total Bike Hires per Month", loc="left", pad=20)
sns.barplot(data=ride_hires_per_month, x=months, y="Total Hires")
plt.show()
