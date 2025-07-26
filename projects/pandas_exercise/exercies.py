import pandas as pd
import numpy as np

# Exercise 1
# Goal: Load student data into a DataFrame, then filter and group it to answer specific questions.
# Setup Code:

# Data for students in different classes
student_data = {
    'Student_ID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Class': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B'],
    'Math_Score': [85, 92, 78, 65, 95, 88, 70, np.nan],
    'Science_Score': [90, 88, 80, 72, 91, 85, np.nan, 87],
    'Attendance_Rate': [0.95, 0.98, 0.85, 0.90, 0.99, 0.92, 0.75, 0.96]
}
students_df = pd.DataFrame(student_data)

# Tasks:
# Calculate the average Math_Score for each Class. (Handle the NaN in Math_Score appropriately).
# Identify students (show their full rows) who have an Attendance_Rate below 0.90.
# Find the student with the highest Science_Score and print their Student_ID.

print(f"Dataframe of Std data:-\n {students_df}")


# nan_values = students_df.isnull()
# nan_values_sum = students_df.isnull().sum()
# print(f"\nNull values:-\n {nan_values_sum}")

# print(students_df.loc[0,'Math_Score'])
# print(students_df['Math_Score'].mean())
filled_std_math_df = students_df['Math_Score'].fillna(students_df['Math_Score'].mean())

ava_math_score = students_df.groupby('Class')['Math_Score'].mean()
print(f"Avarage Math score is:- {ava_math_score}")

attandance_eve = students_df[students_df['Attendance_Rate'] < 0.90]
print(attandance_eve)

max_score_sci = students_df['Science_Score'].idxmax()
student_with_highest_science_score = students_df.loc[max_score_sci, 'Student_ID']
print(f"Highest Score in Science StudentID:- {student_with_highest_science_score}")


# mean_std_math_sci = students_df.mean()
# print(mean_std_math_sci)
# filling_nan_value_wih_mean = nan_values.fillna(mean_std_math_sci)
# print(filling_nan_value_wih_mean)


######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################



# Exercise 2: Advanced Filtering & Data Cleaning (Combined)
# Goal: Practice identifying and handling missing data, and performing conditional filtering.
# Setup Code:

# Sales data for various products and regions
sales_data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Laptop'],
    'Region': ['North', 'South', 'North', 'West', 'East', 'South', 'West', 'East', 'North'],
    'Units_Sold': [10, 25, 15, np.nan, 8, 30, 12, 5, 11],
    'Price_Per_Unit': [1200, 25, 75, 250, 1250, 20, 80, np.nan, 1150],
    'Discount_Applied': [0.1, 0.05, 0.0, 0.15, 0.0, 0.05, 0.1, 0.0, 0.1]
}
sales_df = pd.DataFrame(sales_data)

# Tasks:
# Calculate the Total_Revenue for each sale (Units_Sold * Price_Per_Unit * (1 - Discount_Applied)).
# Find the Product that generated the highest total revenue across all sales.
# Identify all sales (Product, Region, Total_Revenue) in the 'North' region where no Discount_Applied was greater than 0.


unit_sold = sales_df['Units_Sold'].fillna(0)
price_per_unit = sales_df['Price_Per_Unit'].fillna(0)
discount_applied = 1 - sales_df['Discount_Applied']
total_revenue = unit_sold * price_per_unit * discount_applied
sales_df['Total_Revenue'] = total_revenue
print(f"Sales_df:-\n {sales_df}")

#creating A dataFrame of only product adn revenue:-
product_revenue = sales_df[['Product', 'Total_Revenue']]
print("\n", product_revenue)

highest_revenue = sales_df['Total_Revenue'].idxmax()
highest_rev_gen_prod = sales_df.loc[highest_revenue, 'Product']
print(f"\nHighest Revenue Generation Product:- {highest_rev_gen_prod}")

north_sales_no_discount = sales_df[(sales_df['Region'] == 'North') & (sales_df['Discount_Applied'] == 0.0)][['Product', 'Region', 'Total_Revenue']]
print("\nNorth region sales with no discount:\n", north_sales_no_discount)

sales_across_region = sales_df.groupby('Region').agg(
    total_sales =('Total_Revenue', 'mean')
)
print(sales_across_region)


