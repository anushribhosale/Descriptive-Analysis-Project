# Descriptive-Analysis-Project

The code provided performs an initial exploratory data analysis (EDA) on a dataset from the file fortune500.csv.
Here’s a detailed breakdown of each step:

1. Importing Libraries:

Libraries such as pandas, numpy, matplotlib.pyplot, and seaborn are imported for data manipulation and visualization.
Warnings are ignored to avoid cluttering the output.

2. Loading and Inspecting the Dataset:

The dataset is loaded using pd.read_csv().
The shape of the dataset is printed to understand the dimensions.
The first few rows are previewed using df.head().
The dataset summary with data types and non-null counts is obtained using df.info().
Missing values in each column are checked using df.isnull().sum().

3. Descriptive Statistics:

Descriptive statistics for numerical columns are obtained using df.describe().
Descriptive statistics for object (character) columns are obtained using df.describe(include='object').
Descriptive statistics for all columns, regardless of type, are obtained using df.describe(include='all').

4. Measures of Central Tendency for Revenue:

Mean, median, and mode of the 'Revenue (in millions)' column are calculated.
A distribution plot of 'Revenue (in millions)' is created using seaborn.

5. Measures of Dispersion or Variability:

Minimum and maximum values of 'Revenue (in millions)' are identified.
Range, variance, and standard deviation of 'Revenue (in millions)' are computed.
Quartiles (Q1, Q2 (median), Q3) and interquartile range (IQR) are calculated.
A boxplot of 'Revenue (in millions)' is plotted.

6. Measures of Shape of Distribution:

Skewness and kurtosis of 'Revenue (in millions)' are computed to understand the distribution's shape.

7. Handling 'Profit (in millions)' Column:

The 'Profit (in millions)' column's 'N.A' values are replaced with 0.
The column is converted to numeric using pd.to_numeric() with error coercion.

8. Re-check Summary Statistics:

The summary statistics of the cleaned dataset are printed again to reflect the changes after cleaning.


Here's the output you would see for each step:

1. Shape of the dataset:

   Code- Shape of the dataset: (N, M)

where N is the number of rows and M is the number of columns.

2. Preview of the dataset:

   Code- (First few rows of the dataset)

3. Summary of dataset:

   Code- (Info about columns, data types, and non-null counts)

4. Missing values:

   Code- (Count of missing values per column)

5. Descriptive statistics:

   Code- (Descriptive statistics for numerical columns)
         (Descriptive statistics for object columns)
         (Descriptive statistics for all columns)

6. Measures of central tendency:

   Code- Mean Revenue: ...
         Median Revenue: ...
         Mode Revenue: ...

7. Distribution plot:

   A plot showing the distribution of 'Revenue (in millions)'.

8. Measures of dispersion:

   Code- Minimum Revenue: ...
         Maximum Revenue: ...
         Range of Revenue: ...
         Variance of Revenue: ...
         Standard Deviation of Revenue: ...
         Q1: ..., Q2 (Median): ..., Q3: ...
         IQR of Revenue: ...

9. Boxplot:

   A boxplot visualizing the distribution of 'Revenue (in millions)'.

10. Measures of shape:

    Code- Skewness of Revenue: ...
          Kurtosis of Revenue: ...

11. Handling 'Profit (in millions)' column:

    Conversion and replacement of 'N.A' values with 0.

12. Summary statistics after cleaning:

    Code- (Descriptive statistics reflecting cleaned data)

This process will give a comprehensive understanding of the dataset, including its central tendencies, variability, and distribution shapes.

Thank You :)

