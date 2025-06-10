import numpy as np
arr=np.array([1,2,3,4,5]) #converting into array by using .array.
print ("array: ",arr)
print(arr.shape)
print(arr.nbytes)
print(arr.dtype)
values=np.array([[1,2,3,4,5,6],[7,8,9,0,1,2]])
print (values[1,4])#it prints the "1" which is in the 1 row and 4 column, array starts with 0.
arr[2]=9 # changing the value of array
print (arr)
print (values[1,:]) #it will print all the values of column of 1 row, array starts with 0
print (values[:,4]) #it will print all the values of row of 4th column
print (values[0,2:6:2]) # it will print the 0th row values from 1 postion to 4 postion by giving 2 interval
#3 dimentional 
d=np.array([[[1,2,3,4],[5,6,7,8]],[[9,8,7,6],[1,2,3,4]]])
print (d)
print (d[1,0,2]) #it will print the 7 which is in the 1st row in two group and after it will work in 0th row of 1st postion group and choose 7 which is in 2 postion in array.array starts with 0
print(np.zeros((2,5))) # it will print 2 row 5 column matric filled with zero. we can use zeros, ones, rendom, full, identity.

num1=np.array([1,2,3,4,5])
num2=np.array([1,2,3,4,5])
print ("sum: ",num1+num2)
print ("product: ",num1*num2)
print ("sum of product: ",np.sum(num1*num2))
