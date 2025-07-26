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