from array import *
import array as arr #arr is an import

# https://www.educba.com/arrays-in-python/
# typical array index operations
a=arr.array('i', [10 , 20 ,30] ) #declare array
print("Element at 0th index: " , a[0])
print("Element at 1st  index: " , a[1])
print("Element at 2nd index: " , a[2])

#return the value of typecode() in the array
# array.typecode() #syntax

a1 = arr.array('i', [100,200,300] )
#printing array with method
print(a1.typecode)

# insert() syntax
# array.insert(index, element)
a = arr.array('i', [100,200,300])
#inserting a value of 400 to after index 2
a.insert(3, 400);
#looping through array a
for i in a:
print(i)

#creating array
a = arr.array('i', [100,200,300])
#inserting a value of 400 to after index 2
a.insert(3, 400);
#looping through array a
for i in a:
print(i)

