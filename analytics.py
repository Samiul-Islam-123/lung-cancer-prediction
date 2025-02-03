import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("lung_cancer_data.csv")

# Display the first few rows
print(df.head())

# Get basic info about the dataset
print(df.info())

# Summary statistics of numerical columns
print(df.describe())

# Check for missing values
print(df.isnull().sum())
