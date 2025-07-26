import pandas as pd
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
print("\nScores Column:\n", students_df.Score) # Shorthand, works if no spaces in name
print(type(students_df['Name']))  # The result is a Pandas Series.
