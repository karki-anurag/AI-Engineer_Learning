# Create a 3*3 matrix and perform operations:
import numpy as np

matrix_one =  np.arange(1, 10)
print(f"original matrix:- {matrix_one}")

reshape = matrix_one.reshape(3,3)
print(f" Converting into 3*3 Matrix:- {reshape}")

# Transpose:-
transpose = reshape.T
print(f" Transpose of Matrix:- {transpose}")


# extends = matrix_one[:, np.newaxis]
# print(extends)


# Setup Code:
# Daily high temperatures for a week (in Celsius)
# Includes one missing reading (represented by NaN)
daily_temps_c = np.array([28.5, 30.1, 27.9, np.nan, 31.0, 29.8, 28.2])

# Tasks:
# Find the average temperature for the week, ignoring the missing value.
# Find the maximum and minimum temperatures recorded.
# Count how many days had a temperature above 29.0 Celsius (ignoring NaN).

replacing_nan_value = np.nan_to_num(daily_temps_c)
print(f"Replacing Nun value with zero:- {replacing_nan_value}")


ava_temp = np.nanmean(daily_temps_c)
print(f"Avarage Temperature:- {ava_temp}")

max_temp = np.nanmax(daily_temps_c)
print(f"maxmimun Temperature:- {max_temp}")

min_temp = np.nanmin(daily_temps_c)
print(f"Minimum temperature:- {min_temp}")

days_above_twentynine = np.count_nonzero(daily_temps_c > 29.0)
print(f"Days above 29 degree:- {days_above_twentynine}")
