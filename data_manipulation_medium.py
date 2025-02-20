# -*- coding: utf-8 -*-
"""Data_Manipulation_medium.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16ltjUGm9KIpNTiYnwfuORXYzBqYwDDmV
"""

# Install Pandas using pip
!pip install pandas

# Import Pandas
import pandas as pd

# Creating a DataFrame from a dictionary of lists
data = {
    'Name': ['Michael', 'Joseph', 'Blake'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
# Display the DataFrame
print(df)

# Creating a DataFrame from a list of dictionaries
data = [
    {'Name': 'Michael', 'Age': 25, 'City': 'New York'},
    {'Name': 'Joseph', 'Age': 30, 'City': 'Los Angeles'},
    {'Name': 'Blake', 'Age': 35, 'City': 'Chicago'}
]
df = pd.DataFrame(data)
# Display the DataFrame
print(df)

# Load the Iris dataset from a URL
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
df = pd.read_csv(url)

# Display the first few rows of the DataFrame
print(df.head())

# Display the last few rows of the DataFrame
print(df.tail())

# Provide a concise summary of the DataFrame, including data types and non-null counts
print(df.info())

# Generate descriptive statistics for numerical columns
print(df.describe())

# Sort the DataFrame by the 'sepal_length' column
sorted_df = df.sort_values(by='sepal_length')
print("DataFrame sorted by sepal_length:\n", sorted_df.head())

# Subset the DataFrame to include only rows where 'species' is 'setosa'
subset_df = df[df['species'] == 'setosa']
print("\nSubset of DataFrame where species is setosa:\n", subset_df.head())

# Add a new column 'sepal_area' as the product of 'sepal_length' and 'sepal_width'
df['sepal_area'] = df['sepal_length'] * df['sepal_width']
print("DataFrame with new column 'sepal_area':\n", df.head())

# Count the number of each species
species_counts = df['species'].value_counts()
print("\nCount of each species:\n", species_counts)

# Get the proportion of each species
species_props = df['species'].value_counts(normalize=True)
print("\nProportion of each species:\n", species_props)

# Count the number of unique sepal_length values and sort
sepal_length_counts_sorted = df['sepal_length'].value_counts(sort=True)
print("\nCount of each sepal_length value (sorted):\n", sepal_length_counts_sorted)

# Get the proportion of unique sepal_length values and sort
sepal_length_props_sorted = df['sepal_length'].value_counts(sort=True, normalize=True)
print("\nProportion of each sepal_length value (sorted):\n", sepal_length_props_sorted)

# Drop duplicate species/sepal_length combinations
species_sepal = df.drop_duplicates(subset=['species', 'sepal_length'])
print("Unique species and sepal_length combinations:\n", species_sepal.head())

# Drop duplicate species/petal_length combinations
species_petal = df.drop_duplicates(subset=['species', 'petal_length'])
print("\nUnique species and petal_length combinations:\n", species_petal.head())

# Subset the rows where sepal_length is greater than 5.0 and drop duplicate species
large_sepal = df[df['sepal_length'] > 5.0].drop_duplicates('species')
print("\nUnique species with sepal_length > 5.0:\n", large_sepal)

# Introduce some missing values for demonstration
df.loc[0, 'sepal_length'] = None
df.loc[1, 'petal_length'] = None

# Print a DataFrame that shows whether each value is missing or not
print("Missing values in the DataFrame:\n", df.isna())

# Print a summary that shows whether any value in each column is missing
print("\nSummary of missing values in each column:\n", df.isna().any())

# Remove rows with missing values
df_complete = df.dropna()
# Check if any columns contain missing values
print("\nCheck for missing values after dropping rows with NAs:\n", df_complete.isna().any())

# Replace missing values with the mean of the respective columns
df_filled = df.fillna({
    'sepal_length': df['sepal_length'].mean(),
    'petal_length': df['petal_length'].mean()
})
print("\nDataFrame after filling NAs:\n", df_filled.head())

# Load the Iris dataset from a URL again as we have introduced some NA values earlier - Important to run this again
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
df = pd.read_csv(url)

# Calculate cumulative sum of the 'sepal_length' column
cumulative_sum = df['sepal_length'].cumsum()
print("\nCumulative Sum of Sepal Length:\n", cumulative_sum.head())

# Calculate the mean and standard deviation of the 'petal_length' column
mean_petal_length = df['petal_length'].mean()
std_petal_length = df['petal_length'].std()
print("\nMean Petal Length:", mean_petal_length)
print("Standard Deviation of Petal Length:", std_petal_length)

# Group by 'species' and calculate the mean of each group
grouped = df.groupby('species').mean()
print("\nMean Values by Species:\n", grouped)

# Create a pivot table with 'species' as the index and 'sepal_length' as the values
pivot = df.pivot_table(values='sepal_length', index='species', aggfunc='mean')
print("\nPivot Table:\n", pivot)

import pandas as pd
import matplotlib.pyplot as plt

# Plot a histogram of the 'sepal_length' column
df['sepal_length'].plot(kind='hist', bins=20, title='Sepal Length Distribution')
plt.xlabel('Sepal Length')
plt.show()
# Plot a scatter plot of 'sepal_length' vs 'sepal_width'
df.plot(kind='scatter', x='sepal_length', y='sepal_width', title='Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()

import seaborn as sns

# Plot a pairplot of the Iris dataset
sns.pairplot(df, hue='species')
plt.show()
# Plot a boxplot of 'sepal_length' by 'species'
sns.boxplot(x='species', y='sepal_length', data=df)
plt.title('Sepal Length by Species')
plt.show()

