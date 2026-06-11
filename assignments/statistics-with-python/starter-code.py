# Starter Code: Statistics with Python

import numpy as np
import pandas as pd


# Load the dataset
df = pd.read_csv("data.csv")

# Inspect the data
print(df.head())
print(df.info())

# Calculate descriptive statistics with pandas
print(df.describe())

# Pick numeric columns for further analysis
numeric_columns = ["study_hours", "test_score"]

for column in numeric_columns:
    values = df[column]
    print(f"{column} mean: {values.mean():.2f}")
    print(f"{column} median: {values.median():.2f}")
    print(f"{column} std dev: {values.std():.2f}")
    print(f"{column} min: {values.min():.2f}")
    print(f"{column} max: {values.max():.2f}")

# Use numpy for an additional statistic
test_scores = df["test_score"].to_numpy()
print(f"Test score 75th percentile: {np.percentile(test_scores, 75):.2f}")

# Add your written findings below
summary = "Students can compare study hours and test scores to describe patterns in the data."
print(summary)