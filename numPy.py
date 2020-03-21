import numpy as np

#cast normal python list to array
my_list = [1,2,3]
#print(my_list)
arr = np.array(my_list)
#print(arr)

#two dimension array
#list of list
my_mat = [[1,2,3],[4,5,6],[7,8,9]]
#print(np.array(my_mat))

# np.arange return array of range == python range
#print(np.arange(0,11))
#print(np.arange(0,11,2))
#print (np.zeros(3))
#print (np.zeros((5,5)))

#Return a 2-D array with ones on the diagonal and zeros elsewhere
#print(np.eye(3))

#Random values in a given shape. the value will be from zero to one
#print (np.random.rand(3))
#print (np.random.rand(3,3))
#Return random integers from `low` (inclusive) to `high` (exclusive).
#print(np.random.randint(0,100)) # this will return one value like 1 or 14
#print(np.random.randint(0,100,10)) # this will return 10 values from 0 to 10, one dimension array

arr = np.arange(25) # this will make arry from 0 to 24 length  = 25
#print(arr)
#print (arr.shape) # return shape of arrary, indicate one or two dimension
#print(arr.dtype) # return the data type of the content of array
#print(arr.reshape(5,5)) # return the same data of arr but in two dimension arrary

ranarr = np.random.randint(0,15,10)
#print(ranarr)
#print(ranarr.max())
#print(ranarr.argmax())
#print(ranarr.min())
#print(ranarr.argmin())

#from numpy.random import randint
#print (randint(3,10))

#2 D array
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2d)
#print (arr_2d[0][0]) # will print first element = 5
#print (arr_2d[0,0])
#print (arr_2d[1][1]) # will print the value  = 25
#print (arr_2d[1,1])
#print(arr_2d[:2,1:])

#condions in arrary -- condtional selection
arr = np.arange(0,11)
#print(arr)
#print(arr[arr > 5])

arr_2d = np.arange(50).reshape(5,10)
#print (arr_2d)
#print(arr_2d[1:3,3:5]) 

#NumPy Operation
# array with arry
arr = np.arange(0,11)
print(arr)
print (arr + arr)
print (arr - arr)
#print (arr / arr)

# array wtih Scalars
print(arr)
print(arr*2)

# array with Universal Array Function
print (np.sqrt(arr))
print (np.exp(arr))
print (np.max(arr))