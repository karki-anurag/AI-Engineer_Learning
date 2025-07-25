#numpy which is also called Numerical Python
""" 
Numpy is like a SUper Calculator you have to perform different Numerical Operation in python.
1) why not regular python?
As we know Python contains List which is not that much of flexible. so, to tackel that we use Numpy
because it contains Array.

2) why Numpy?
 a)It's super fast in term of numerical operation.
 b)It's contains Array instead of list which is much more flexiable than list.
 c)Easy Math operation like example if you have 10 numbers in a Array 
    and you want to add 10 to each number just do num_array+ 10. no need to go through each number.
 """

import numpy as np
#Array:
#1D Array:
arr = np.array([10, 20, 30])
print(f" One dimensasion array:- {arr}")
print(f" Type of array:- {type(arr)}")

#2D Array: In this array we have bot row and coloum inside a list.
arr_two_d = np.array([[10, 20],
               [30,40],
               [80,90]])
print(f" Two dimensasion array:- {arr_two_d}")

#Easy math Examples:
arr_add = np.array([10, 20, 30])
# i want to add 5 in each of my values:
#we can perform multiplication as well:
new_arr = arr_add + 5
new_mul_arr = arr_add * 5
print(f" adding 5 to each array:- {new_arr}")
print(f" Muntiplying each array by 5 :-{new_mul_arr}")

# This is just like Matrix, we can add muntiples array lists:
arr_one = np.array([10, 20, 30])
arr_two = np.array([40, 50, 80])
sum_arr = arr_one + arr_two
print(f" adding two array :-{sum_arr}")


#Some build-in functions of Array:-
arr_three_d = np.array([[10, 20, 45],
                     [30,40, 55],
                     [80,90, 95]])

arr_one_d = np.array([10, 20, 30])

shape = arr_one_d.shape
size_of_array = arr_three_d.size
dimension = arr_three_d.ndim

print(f"Size of the array:- {size_of_array}")
print(f"Shape of the array:- {shape}")
print(f"Dimension of the array:- {dimension}")


#Indexing and Slicing of Arrays:-
arr_three_d_indexing_slicing = np.array([[10, 20, 45],
                                 [30,40, 55],
                                 [80,90, 95]])
#indexing always start from Zero.
data_from_Secondrow_firstColoum = arr_three_d_indexing_slicing[1,0]

#Silicing:- [row_start:row_end, col_start:col_end]
data_from_zeroindex_to_secondindex = arr_three_d_indexing_slicing[0:2,:]
print(f"silicing Value from 2D array:- {data_from_zeroindex_to_secondindex}")
print(f"Indexing Value from 2D array:- {data_from_Secondrow_firstColoum}")

#Array with the range of Numbers-
range_array = np.arange(10)
even_numbers = np.arange(2, 12, 2) # Start at 2, go up to (not including) 12, step by 2
print(range_array)
print(even_numbers)


#Common Numpy Operations:-
arr = np.array([85, 90, 78, 92, 88])
print("Sum of scores:", np.sum(arr))
print("Average score:", np.mean(arr))
print("Highest score:", np.max(arr))
print("Lowest score:", np.min(arr))
print("Standard deviation:", np.std(arr)) 