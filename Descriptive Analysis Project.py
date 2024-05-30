# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Ignore warnings
import warnings
warnings.filterwarnings('ignore')
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

# Load the dataset
df = pd.read_csv('fortune500.csv')

# View dimensions of dataset
print(f"Shape of the dataset: {df.shape}")

# Preview the dataset
print(df.head())

# View summary of dataset
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Descriptive statistics with describe() function
# Summary statistics of numerical columns
print(df.describe())

# Summary statistics of character columns
print(df.describe(include='object'))

# Summary statistics of all the columns
print(df.describe(include='all'))

# Computation of measures of central tendency
# Mean of Revenue (in millions)
mean_revenue = df['Revenue (in millions)'].mean()
print(f"Mean Revenue: {mean_revenue}")

# Median of Revenue (in millions)
median_revenue = df['Revenue (in millions)'].median()
print(f"Median Revenue: {median_revenue}")

# Mode of Revenue (in millions)
mode_revenue = df['Revenue (in millions)'].mode()[0]
print(f"Mode Revenue: {mode_revenue}")

# Observation: Distribution plot of Revenue (in millions)
sns.distplot(df['Revenue (in millions)'], bins=10, hist=True, kde=True, label='Revenue (in millions)')
plt.legend()
plt.show()

# Computation of measures of dispersion or variability
# Minimum value of Revenue (in millions)
min_revenue = df['Revenue (in millions)'].min()
print(f"Minimum Revenue: {min_revenue}")

# Maximum value of Revenue (in millions)
max_revenue = df['Revenue (in millions)'].max()
print(f"Maximum Revenue: {max_revenue}")

# Range of Revenue (in millions)
range_revenue = max_revenue - min_revenue
print(f"Range of Revenue: {range_revenue}")

# Variance of Revenue (in millions)
variance_revenue = df['Revenue (in millions)'].var()
print(f"Variance of Revenue: {variance_revenue}")

# Standard deviation of Revenue (in millions)
std_revenue = df['Revenue (in millions)'].std()
print(f"Standard Deviation of Revenue: {std_revenue}")

# Q1, Q2 (median), Q3 of Revenue (in millions)
Q1 = df['Revenue (in millions)'].quantile(0.25)
Q2 = df['Revenue (in millions)'].quantile(0.5)
Q3 = df['Revenue (in millions)'].quantile(0.75)
print(f"Q1: {Q1}, Q2 (Median): {Q2}, Q3: {Q3}")

# Interquartile Range (IQR)
IQR = Q3 - Q1
print(f"IQR of Revenue: {IQR}")

# Boxplot of Revenue (in millions)
plt.figure(figsize=(10, 6))
sns.boxplot(y=df['Revenue (in millions)'])
plt.title('Boxplot of Revenue (in millions)')
plt.show()

# Computation of measures of shape of distribution
# Skewness of Revenue (in millions)
skewness_revenue = df['Revenue (in millions)'].skew()
print(f"Skewness of Revenue: {skewness_revenue}")

# Kurtosis of Revenue (in millions)
kurtosis_revenue = df['Revenue (in millions)'].kurt()
print(f"Kurtosis of Revenue: {kurtosis_revenue}")

# Handling 'Profit (in millions)' column
# Replace 'N.A' with 0 and convert to numeric
df["Profit (in millions)"] = df["Profit (in millions)"].replace('N.A', 0)
df["Profit (in millions)"] = pd.to_numeric(df["Profit (in millions)"], errors='coerce')

# Check the summary again after data cleaning
print(df.describe())