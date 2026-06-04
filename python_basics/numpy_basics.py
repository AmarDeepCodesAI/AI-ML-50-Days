import numpy as np;

numbers = [10, 10.54,"amar", True,30, 40, 50]

print(numbers)

# NumPy is a Python library used for numerical 
# computing and multidimensional array operations.
#  It provides faster performance than Python 
# lists and is widely used in Data Science, Machine Learning, and AI.

# NumPy Arrays
# A NumPy array is a powerful data structure that
#  allows for efficient storage and manipulation 
# of large datasets. It is similar to a Python 
# list but provides additional functionality and performance benefits.

array = np.array([10, 20, 30, 40, 50])

print("array->",array) #` Output: [10 20 30 40 50], which is a NumPy array containing the elements from the original list.`
print("Type of array->", type(array)) # Output: <class 'numpy.ndarray'>, which indicates that the variable 'array' is a NumPy array.
# NumPy arrays are homogeneous, meaning they can only store elements of the same data type.
# If you try to create a NumPy array with mixed data types, it will automatically convert all elements to a common data type (usually the most general one) to maintain homogeneity.
mixed_array = np.array([10, 20.5, "Hello", True])

print("mixed_array->", mixed_array)# Output: ['10' '20.5' 'Hello' 'True'], all elements are converted to strings due to the presence of a string element.
print("Type of mixed_array->", type(mixed_array)) # Output: <class 'numpy.ndarray'>, but all elements are of type string due to the presence of a string element.

#ndarray
# The ndarray (n-dimensional array) is the core data structure in NumPy.

#shape
# The shape of a NumPy array refers to the dimensions of the array.

print("Shape of array->", array.shape) # Output: (5,), which indicates that the array has 5 elements in a single dimension.

two_darray = np.array([[1, 2, 3], 
                       [4, 5, 6]])
print("shape of two_darray->", two_darray.shape) # Output: (2, 3), which indicates that the array has 2 rows and 3 columns.

thee_darray = np.array([[[1, 2], [3, 4]],
                        [[5, 6], [7, 8]]])
print("shape of thee_darray->", thee_darray.shape) # Output: (2, 2, 2), which indicates that the array has 2 blocks, each containing 2 rows and 2 columns.

#ndim
# The ndim attribute of a NumPy array indicates the number of dimensions (axes) the array has.

print("Number of dimensions in array->", array.ndim) # Output: 1, which indicates that the array is one-dimensional.
print("Number of dimensions in two_darray->", two_darray.ndim) # Output: 2, which indicates that the array is two-dimensional.
print("Number of dimensions in thee_darray->", thee_darray.ndim) # Output: 3, which indicates that the array is three-dimensional.


arr1 = np.array([5, 10, 15, 20])

arr2 = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

print(arr1)
print(arr1.shape)
print(arr1.ndim)

print(arr2) # Output: [[1 2]
             #          [3 4]
             #          [5 6]]
print(arr2.shape) # Output: (3, 2), which indicates that the array has 3 rows and 2 columns.
print(arr2.ndim) # Output: 2, which indicates that the array is two-dimensional.