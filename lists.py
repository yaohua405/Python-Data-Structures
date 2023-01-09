from typing import List
#To be able to annotate what types your list should accept, you need to use typing.List
'''
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, 
all with different qualities and usage.
Lists are created using square brackets:
'''

#Since lists are indexed, lists can have items with the same value:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#To determine how many items a list has, use the len() function:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#List items can be of any data type, AND include different data types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list1 = ["abc", 34, True, 40, "male"]

#show data type of the list
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#using a list constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)