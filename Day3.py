# import numpy

print("=======import numpy=======")
import numpy as np
print()


#create 1D array
print("=======create a 1d array=======")
arr = np.array([1, 2, 3 , 4, 5, 6])
print(arr)
print()

#create a 2D array
print("=======create a 2D array=======")
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print()

#create a 3D array
print("=======create a 3D array=======")
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr)
print()

# array properties
print("=======array properties=======")
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("shape:", arr.shape)
print("dimensions:", arr.ndim)
print("size:", arr.size)
print("data type:", arr.dtype)
print()


# create an array of zeros
print("=======create an array of zeros=======")
arr = np.zeros((3, 4))
print(arr)
print()

# create an array of ones
print("=======create an array of ones=======")
arr = np.ones((2, 3))
print(arr) 
print()

#create an array of range
print("=======create an array of range=======")
arr = np.arange(1, 10)
print(arr)
print()


#array of indexing and slicing
print("=======array of indexing and slicing=======")
arr = np.array([1, 2, 3 ,4, 5, 6])
print(arr[0])  # access the first element
print(arr[1])  # access the second element
print(arr[1:4])  # slice the array from index 1 to 3
print()


#array operations
print("=======array operations=======")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("addition:", a + b)
print("subtraction:", a - b)
print("multiplication:", a * b)
print("division:", a / b)
print()


#mathematical functions
print("=======mathematical functions=======")
arr = np.array([10, 20, 30, 40, 50])
print("sum:", arr.sum())
print("mean:", arr.mean())
print("standard deviation:", arr.std())
print("maximum:", arr.max())
print("minimum:", arr.min())
print()


# square and square root
print("=======square and square root=======")
arr = np.array([1, 2, 3, 4, 5])
print("square:", arr ** 2)
print("square root:", np.sqrt(arr))
print()


#sorting, reshape and random numbers
print("=======sorting, reshape and random numbers=======")
arr = np.array([3, 1, 4, 2, 5])
print("sorted:", np.sort(arr))
print("reshaped:", arr.reshape(5, 1))
print("random numbers:", np.random.randint(5))
print()


#practise program
print("=======practise program=======")
arr = np.array([1, 2, 3 ,4, 5, 6])
print("array:", arr)
print("sum:", arr.sum())
print("mean:", arr.mean())
print()

print("square:", arr ** 2)
print("square root:", np.sqrt(arr))
print()

print("sorted:", np.sort(arr))
print()

a=np.array([1, 2, 3])
b=np.array([4, 5, 6])
print("addition:", a + b)
print("subtraction:", a - b)
print("multiplication:", a * b)
print("division:", a / b)