import numpy 

oneDiemnsionArray=numpy.array([1,2,3,4,5,7])
# print(oneDiemnsionArray[1::2])

a = numpy.array([[1,2,3],[3,4,5],[4,5,6]]) 
print(a)
print (a[...,0:3:2])  # this returns array of items in the second column 
print (a[1,...])   # Now we will slice all items from the second row 
print (a[...,1:])  # Now we will slice all items from column 1 onwards 




