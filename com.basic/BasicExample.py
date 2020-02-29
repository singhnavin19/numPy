import numpy as np
# a=np.array
# print(a)

# # numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)  
# 1    object    It represents the collection object. It can be a list, tuple, dictionary, set, etc.
# 2    dtype    We can change the data type of the array elements by changing this option to the specified type. The default is none.
# 3    copy    It is optional. By default, it is true which means the object is copied.
# 4    order    There can be 3 possible values assigned to this option. It can be C (column order), R (row order), or A (any)
# 5    subok    The returned array will be base class array by default. We can change this to make the subclasses passes through by setting this option to true.
# 6    ndmin    It represents the minimum dimensions of the resultant array.

a1=np.array([1.1,2,3,8,9],float) #1d array
# print(a1)
# print(a1[1])  #to accesss each element
# print("dimension of a1",a1.ndim) #dimension
# print(a1.itemsize) #to get size of each element
# print(a1.dtype)   #to get the size of string element   #string <U1 
#                   
# For a 1D array, the shape would be (n,) where n is the number of elements in your array.
                # For a 2D array, the shape would be (n,m) where n is the number of rows and m is the number of columns in your array.
# a1=a1.reshape(3,1) print(a1)   print(a1.shape)
# a = np.arange(10) 
# print(a)
# b = a[2:7:2]
# print(b) 


a2=np.array([[1,2],[2,3],[6,7]]) #2d array
# print(a2) 
# print(a2[0,0])             
# print("dimension of a2",a2.ndim)              
# print(a2.itemsize) 
# print(a2.dtype)   #to get the size of string element   #string <U1 
print(a1.shape)  #tp get shape and size[row,column ] 
print(a1.size)
print(a2.shape)  #tp get shape and size 
print(a2.size)







#  
# import sys #get Size of primitive datat Type
# # x=[100,200,300,400]
# x11=1
# # print(sys.getsizeof(x))  # //44
# print(sys.getsizeof(x11))
# x1=np.array([1,2])
# print(x1.itemsize)  #//4
