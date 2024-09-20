# -*- coding: utf-8 -*-
"""TestTwo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DiRE0q85st2udMxe1JQazL8VbFBAwsXt

1. Perform data inspection and identify any missing or inconsistent values.
"""

import pandas as pd

#load dataset
file_path = '/content/Test2_dataset.xlsx'

#read the Excel file into a Pandas DataFrame
df = pd.read_excel(file_path)

#show first few rows
#print(df.head())

# Check for missing values in the dataset and print the total number of missing values for each column
missing_data = df.isnull().sum()

# Print the result
print("Total number of missing values for each column:")
print(missing_data)

"""2. Handle any missing data using appropriate techniques (e.g., fill missing values or remove incomplete rows)."""

#replace ch4 conversion, co2 conversion, and syngas_ratio columns with means
#remove ni dispersion column since too many valuesa are missing

#imputing missingvalues with mean
df['CH4 Conversion'].fillna(df['CH4 Conversion'].mean(), inplace=True)
df['CO2 Conversion'].fillna(df['CO2 Conversion'].mean(), inplace=True)
df['Syngas_Ratio'].fillna(df['Syngas_Ratio'].mean(), inplace=True)

#remove ni dispersion column
df_cleaned = df.dropna()

# Check again for missing values in the dataset and print the total number of missing values for each column
missing_data = df_cleaned.isnull().sum()

# Print the result
print("Total number of missing values for each column:")
print(missing_data)

"""3. Apply data transformation techniques, such as normalization or encoding categorical variables, to prepare the data for machine learning tasks."""

#identify catergorical columns
categorical_columns = df_cleaned.select_dtypes(include=['object']).columns

#display categorical columns
categorical_columns

#apply one-hot encoding to categorical variables
df_encoded = pd.get_dummies(df_cleaned,columns=categorical_columns,drop_first=True)

#display the first few rows of the encoded dataset
df_encoded.head()

"""4. Generate summary statistics (mean, median, standard deviation, etc.) for the dataset."""

# Calculate statistics for numeric columns
numeric_cols = df_cleaned.select_dtypes(include='number')

# Mean
mean_values = numeric_cols.mean()

# Median
median_values = numeric_cols.median()

# Standard Deviation
std_values = numeric_cols.std()

# Min and Max
min_values = numeric_cols.min()
max_values = numeric_cols.max()

# Interquartile Range (IQR)
Q1 = numeric_cols.quantile(0.25)
Q3 = numeric_cols.quantile(0.75)
iqr_values = Q3 - Q1

# Display the results
stats_summary = pd.DataFrame({
    'Mean': mean_values,
    'Median': median_values,
    'Standard Deviation': std_values,
    'Min': min_values,
    'Max': max_values,
    'Interquartile Range (IQR)': iqr_values
})

print(stats_summary)

"""5. Create visualizations (scatter plots, histograms, box plots) to identify trends and relationships between variables.
6. Analyze the correlations between features and target variables (CH₄ Conversion, CO₂ Conversion, and Syngas Ratio).
"""

import seaborn as sns
import matplotlib.pyplot as plt

#create scatter plots relating chosen variables to CH4 Conversion
#temperature
sns.scatterplot(x='Reaction Temperature', y='CH4 Conversion', data=df_cleaned)
plt.title('Scatter Plot of Reaction Temperature vs. CH4 Conversion')
plt.xlabel('Reaction Temperature')
plt.ylabel('CH4 Conversion')
plt.show()

#rxn time
sns.scatterplot(x='Reaction Time', y='CH4 Conversion', data=df_cleaned)
plt.title('Scatter Plot of Reaction Time vs. CH4 Conversion')
plt.xlabel('Reaction Time')
plt.ylabel('CH4 Conversion')
plt.show()

#pore size
sns.scatterplot(x='Pore Size', y='CH4 Conversion', data=df_cleaned)
plt.title('Scatter Plot of Pore Size vs. CH4 Conversion')
plt.xlabel('Pore Size')
plt.ylabel('CH4 Conversion')
plt.show()

#surface area
sns.scatterplot(x='Surface Area', y='CH4 Conversion', data=df_cleaned)
plt.title('Scatter Plot of Surface Area vs. CH4 Conversion')
plt.xlabel('Surface Area')
plt.ylabel('CH4 Conversion')
plt.show()

#Ni Loading (nickel content)
sns.scatterplot(x='Ni Loading', y='CH4 Conversion', data=df_cleaned)
plt.title('Scatter Plot of Ni Loading vs. CH4 Conversion')
plt.xlabel('Nickel Content of the Catalyst')
plt.ylabel('CH4 Conversion')
plt.show()

"""As temp increased, CH4 Conversion increased

As reaction time increased, CH4 Conversion increased

As pore size increased, CH4 Conversion slightly increased

There is no notable correlation between surface area and CH4 Conversion

As Nickel content of the catalyst increased, CH4 Conversion increased
"""

import seaborn as sns
import matplotlib.pyplot as plt

#create scatter plots relating chosen variables to CO2 Conversion
#temp
sns.scatterplot(x='Reaction Temperature', y='CO2 Conversion', data=df_cleaned)
plt.title('Scatter Plot of Reaction Temperature vs. CO2 Conversion')
plt.xlabel('Reaction Temperature')
plt.ylabel('CO2 Conversion')
plt.show()

#rxn time
sns.scatterplot(x='Reaction Time', y='CO2 Conversion', data=df_cleaned)
plt.title('Scatter Plot of Reaction Time vs. CO2 Conversion')
plt.xlabel('Reaction Time')
plt.ylabel('CO2 Conversion')
plt.show()

#pore size
sns.scatterplot(x='Pore Size', y='CO2 Conversion', data=df_cleaned)
plt.title('Scatter Plot of Pore Size vs. CO2 Conversion')
plt.xlabel('Pore Size')
plt.ylabel('CO2 Conversion')
plt.show()

#surface area
sns.scatterplot(x='Surface Area', y='CO2 Conversion', data=df_cleaned)
plt.title('Scatter Plot of Surface Area vs. CO2 Conversion')
plt.xlabel('Surface Area')
plt.ylabel('CO2 Conversion')
plt.show()

#Ni Loading
sns.scatterplot(x='Ni Loading', y='CO2 Conversion', data=df_cleaned)
plt.title('Scatter Plot of Ni Loading vs. CO2 Conversion')
plt.xlabel('Nickel Content of the Catalyst')
plt.ylabel('CO2 Conversion')
plt.show()

"""As temp increased, CO2 Conversion increased

As reaction time increased, CO2 Conversion increased

As pore size increased, CO2 Conversion slightly increased

There is no notable correlation between surface area and CO2 Conversion

As Nickel content of the catalyst increased, CO2 Conversion increased
"""

import seaborn as sns
import matplotlib.pyplot as plt

#create scatter plots relating chosen variables to Syngas Ratio
#temp
sns.scatterplot(x='Reaction Temperature', y='Syngas_Ratio', data=df_cleaned)
plt.title('Scatter Plot of Reaction Temperature vs. Syngas Ratio')
plt.xlabel('Reaction Temperature')
plt.ylabel('Syngas Ratio')
plt.show()

#rxn time
sns.scatterplot(x='Reaction Time', y='Syngas_Ratio', data=df_cleaned)
plt.title('Scatter Plot of Reaction Time vs. Syngas Ratio')
plt.xlabel('Reaction Time')
plt.ylabel('Syngas Ratio')
plt.show()

#pore size
sns.scatterplot(x='Pore Size', y='Syngas_Ratio', data=df_cleaned)
plt.title('Scatter Plot of Pore Size vs. Syngas Ratio')
plt.xlabel('Pore Size')
plt.ylabel('Syngas Ratio')
plt.show()

#surface area
sns.scatterplot(x='Surface Area', y='Syngas_Ratio', data=df_cleaned)
plt.title('Scatter Plot of Surface Area vs. Syngas Ratio')
plt.xlabel('Surface Area')
plt.ylabel('Syngas Ratio')
plt.show()

#Ni Loading
sns.scatterplot(x='Ni Loading', y='Syngas_Ratio', data=df_cleaned)
plt.title('Scatter Plot of Ni Loading vs. Syngas Ratio')
plt.xlabel('Nickel Content of the Catalyst')
plt.ylabel('Syngas Ratio')
plt.show()

"""As temp increased, the Syngas Raio increased

As reaction time increased, the Syngas Raio increased

As the pore size increased, the Syngas Ratio slightly increased

The surface area and Syngas Ratio show no notable trends

As the nickel content in the catalyist increased, the Syngas Ratio slightly increased
"""