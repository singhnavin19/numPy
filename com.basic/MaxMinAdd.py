a=[[1,2],[8,3]]
b=[]
for x in a:
    for y in x:
        b.append(y)
print(max(b))        
         


import numpy as np  
a = np.array([[1,2],[3,10],[15,4]])  
print("The array:",a)  
print("The maximum element:",a.max())  
print("The minimum element:",a.min())  
print("The sum of the elements:",a.sum())  
