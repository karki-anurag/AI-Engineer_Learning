import pandas as pd
import numpy as np
"""
What is Pandas?
Pandas is a powerful data manipulation and analysis library for Python,
providing data structures like Series and DataFrame that make it easy to work with structured data.
 Series:- one dimensional array with labels.
 DataFrame:- two dimensional array with labels for both rows and columns.

why Pandas?
Handles Tabular Data: Perfect for data that comes in rows and columns.
Easy Data Loading: Reads data from various formats (CSV, Excel, SQL databases, etc.) with simple commands.
Data Cleaning: Excellent tools for handling missing data, duplicates, and inconsistent formats.
Data Transformation: Effortlessly reshape, combine, filter, and aggregate data.
Time Series Functionality: Powerful tools for working with time-stamped data.
Built on NumPy: Leverages NumPy's speed and efficiency for numerical operations.
"""
#Basic Concepts of Pandas:
variable = pd.Series([10, 20, 30, 40, 50])
print(f"Series:-\n {variable}")

# Access by position (0-based)
print("\nFirst Variable:", variable[0]) 

# Giving custom labels (index)
daily_temps = pd.Series([25, 27, 26, 28, 24],
                        index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
print("\nDaily Temperatures:\n", daily_temps)

# Access by label
print("\nTemperature on Wednesday:", daily_temps['Wednesday'])
# Access multiple elements by label
print("\nTemps for Mon, Wed, Fri:\n", daily_temps[['Monday', 'Wednesday', 'Friday']])

##################################################################################################

# DataFrame Example
#Keys become column-(names) and values are lists of data.
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 22, 35, 28],
    'City': ['New York', 'London', 'Paris', 'New York', 'Tokyo'],
    'Score': [85, 92, 78, 95, 88]
}
students_df = pd.DataFrame(data)
print("Students DataFrame:\n", students_df)

#properties of Pandas DataFrame
print("\nDataFrame Shape (rows, columns):", students_df.shape)
print("DataFrame Columns:", students_df.columns)
print("DataFrame Index:", students_df.index)
print("DataFrame Data Types:\n", students_df.dtypes)

# Selecting Data in DataFrames
print("\nNames Column:\n", students_df['Name'])
print(f"Datatype:- {type(students_df['Name'])}")  # The result is a Pandas Series.
print("\nScores Column:\n", students_df.Score) # Shorthand, works if no spaces in name
print("\nNames and Ages:\n", students_df[['Name', 'Age']]) #The result is another DataFrame.


#############################################################################################
# Selecting Rows using .loc (by label) and .iloc (by position):
"""
.loc[row_label, column_label] - Labels are used to access rows and columns.
.iloc[row_position, column_position] - Integer positions are used to access rows and columns.
"""
# Using .loc (by label/index)
print("\nRow with index 2:\n", students_df.loc[1])
print("\nAlice's Score using .loc:", students_df.loc[0, 'Score'])

# Using .iloc (by integer position)
print("\nFirst row using .iloc:\n", students_df.iloc[0]) # Alice's row
print("\nThird row, second column (Age of Charlie):", students_df.iloc[2, 1])

# Slicing rows with .loc (inclusive of end label)
print("\nRows from index 1 to 3 (inclusive) using .loc:\n", students_df.loc[1:3])

# Slicing rows with .iloc (exclusive of end position)
print("\nRows from position 1 to 3 (exclusive) using .iloc:\n", students_df.iloc[1:4])
################################################################################################

#Filtering DataFrames

older_students = students_df[students_df['Age'] > 25]
print("\nOlder Students (Age > 25):\n", older_students)

# Students from 'New York' AND with a score above 90
smart_ny_students = students_df[(students_df['City'] == 'New York') & (students_df['Score'] > 90)]
print("\nSmart students from New York:\n", smart_ny_students)

# Students from 'New York' OR 'London'
ny_or_london_students = students_df[students_df['City'].isin(['New York', 'London'])]
print("\nStudents from NY or London:\n", ny_or_london_students)


################################################################################################
################################################################################################
################################################################################################
# Intermiidiate concepts of Pandas:-

#NaN Values Handling:-
data_with_nan = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [6, np.nan, 8, 9, 10],
    'C': [11, 12, 13, 14, np.nan]
}

df_nan = pd.DataFrame(data_with_nan)
print("\nDataFrame with NaN values:\n", df_nan)

# Check for missing values
print("\nIs NaN (element-wise):\n", df_nan.isnull())
print("\nNumber of missing values per column:\n", df_nan.isnull().sum())

""" 
We Have Three approach to handle NaN values:
1. Drop rows/columns with NaN values.
2. Fill NaN values with a specific value (like 0 or mean).
3. Interpolate to estimate missing values based on surrounding data.
"""

# # Drop rows with any missing values
# df_dropped_rows = df_nan.dropna()
# print("\nDataFrame after dropping rows with NaNs:\n", df_dropped_rows)

# # Drop columns with any missing values
# df_dropped_cols = df_nan.dropna(axis=1) # axis=1 means columns
# print("\nDataFrame after dropping columns with NaNs:\n", df_dropped_cols)

# # Fill missing values
# df_filled_zero = df_nan.fillna(0)
# print("\nDataFrame after filling NaNs with 0:\n", df_filled_zero)

# You'd typically fill each column with its own mean or median
# Fill NaNs with the mean of the column (common imputation strategy)
means = df_nan.mean()
print("\nColumn Means:\n", means)
df_filled_mean = df_nan.fillna(df_nan.mean()) # This will calculate mean for each row and fill NaNs accordingly
print("\nDataFrame after filling NaNs with column means:\n", df_filled_mean)

######################################################################################################
# Grouping DataFrames:-
# groupby():- This is one of the most powerful features for summarizing data by categories.

print("\nOriginal Students DataFrame:\n", students_df)
# Group by 'City' and calculate the average 'Score' for each city
avg_score_by_city = students_df.groupby('City')['Score'].mean()
print("\nAverage Score by City:\n", avg_score_by_city)

# Group by 'City' and count number of students, also get average age and score
city_summary = students_df.groupby('City').agg(
    total_students=('Name', 'count'), # count non-NaN values in 'Name'
    average_age=('Age', 'mean'),
    max_score=('Score', 'max')
)
print("\nCity Summary:\n", city_summary)

###############################################################################################

#Merging/Joining Datafrmames:
# Create another DataFrame for subjects
subjects_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Eve', 'David'],
    'Favorite_Subject': ['Math', 'Science', 'History', 'Art', 'Physics']
}
subjects_df = pd.DataFrame(subjects_data)
print("\nSubjects DataFrame:\n", subjects_df)
# Merge students_df and subjects_df on the 'Name' column
merged_df = pd.merge(students_df, subjects_df, on='Name', how='outer')
print("\nMerged DataFrame (Inner Join):\n", merged_df)

# types of joins:
# how ='inner': only keep rows where 'Name' exists in BOTH DataFrames
# how='left': Keep all rows from left DataFrame, add matching from right.
# how='right': Keep all rows from right DataFrame, add matching from left.
# how='outer': Keep all rows from both DataFrames, fill NaNs where no match.

########################################################################################

#WE can also use the custom function to apply on DataFrame:
# Function to categorize age
def age_category(age):
    if age < 18:
        return 'Minor'
    elif age < 30:
        return 'Young Adult'
    else:
        return 'Adult'

students_df['Age_Category'] = students_df['Age'].apply(age_category)
print("\nDataFrame with Age Category:\n", students_df)

#################################################################################################

# Commonly Used Pandas Functions/Methods in EDA
# df.head(n) / df.tail(n): View the first/last n rows. Essential for a quick look at your data.
print(students_df.head(2)) 
print(students_df.tail(1)) 
# df.info(): Provides a concise summary of a DataFrame, including data types, non-null values, and memory usage. Super helpful for initial data quality checks.
print(students_df.info())

# df.describe(): Generates descriptive statistics for numerical columns, including count, mean, std, min, max, and percentiles. Great for understanding distributions.
print(students_df.describe())

# df.value_counts(): Counts unique values in a Series, useful for categorical data analysis.
print(students_df['City'].value_counts())

# df.isnull().sum(): As shown above, quickly identify the number of missing values per column.
print("\nMissing values per column:\n", students_df.isnull().sum())

# df.duplicated() / df.drop_duplicates(): Identify and remove duplicate rows.
print("\nDuplicated Rows:\n", students_df.duplicated())

# df.sort_values(by='column_name'): Sort DataFrame by a specific column.

#df.corr(): Calculate pairwise correlation of columns, useful for understanding relationships between numerical variables.
print("\nCorrelation Matrix:\n", students_df.corr())

""" 
df.groupby() (with aggregations): As explained above, for summary statistics across categories.

df.pivot(): Reshape data to create a new DataFrame with specified index and columns.

df.pivot_table(): A more advanced way to summarize and rearrange data, allowing you to create 
"pivot tables" similar to Excel.
"""
