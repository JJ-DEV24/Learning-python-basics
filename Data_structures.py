"""Sets"""

# Definition: Sets are a data structure that contains multiple elements in {}.
# They are unordered and unchangeable, although you can add or remove its values
# using the functions .add() and .remove() respectively.

colours= {'blue', 'red', 'green', 'purple', 'purple'}
fave_colours={'blue', 'green', 'orange', 'orange', 'white', 'black', 'white'}

# Set methods
""".add() - adds a value to a set
.remove() - removes a value from a set (and informs you if the value does not exist in set (i.e. key value error))
.intersection() - returns a set with duplicates from two sets
.intersction update() - removes items that are not duplicates in two sets
.union() - returns a set which contains a combination of two other sets
.pop() - removes an element from a set and returns the value
.clear() - removes all the values from a set
.copy() - returns a copy of a set
.difference() - returns a set containing the difference between two or more sets
.discard() - removes specifed item from a set (does not inform you if the value does not exisit (i.e. key value error))
.difference update() - removes items in a set that are also included in another set
.idisjoint() - returns True if none of the items are present in both sets, otherwise it returns False.
.issubset() - returns whetehr another set contains this set or not
.issuperset() - returns whether this set contains another set
.symetrice_difference() - returns all the items present in given sets, except the items in their intersections
.symetric_difference_update() - inserts the symmetric differences from this set and another
.update() - update the set with the union of this set and others"""

print(fave_colours.intersection(colours))
print(colours.union(fave_colours))
for colours in colours:
    print(colours)
colours.isdisjoint(fave_colours)
colours.issubset(fave_colours)

# Challenge: Write a function merge.arrays(), that takes two lists of integers as inputs combines them,
# removes duplicates, sorts the combines lst and returns it
def merge_arrays(list1, list2):
    list3 = list1 + list2
    list4 = set(list3)
    list5 = list(list4)
    sorted(list5)
    return(list5)


merge_arrays(list1, list2)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 27]

# Simplified
def merge_arrays(list1, list2):
    return sorted(set(list1 + list2))

merge_arrays(list1, list2)
Out[19]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 27]






"""Dictionaries"""

#Defintion: Dictionaries are data structures that contain collection of elements.
# These elements are changeable and ordered. Note dictionaries do not contain duplicates

patient_1= {'name': 'Terry', 'age': 34, 'address': '555 North Road, London, E13 243', 'number': '07908603982'}
patient_2= {'name': 'Tanya', 'age': 56, 'address': '777 South Road, Barking, IG11 2OP', 'number': '07493768273'}

# Dictionary Methods
.clear() - Clears all the elements from the dictionary
.copy() - Returns a copy of the dictionary
.fromkeys()  -Returns a dictionary with the specified keys and the specified value.
# e.g.
x= ('type 1', 'type 2', 'type 3')
y= 0
x_and_y_dict={}
x_and_y_dict.fromkeys(x,y)
Out[65]: {'type 1': 0, 'type 2': 0, 'type 3': 0}
.get()  - Returns the value of the specified key
.items() - Returns a list containing a tuple of each key value pair
.keys() - Returns a list containg the dictionary keys
.pop() - Removes the element with the specified key
.popitem() - Removes the last key value pair in a dictionary
.setdefault() - returns the value of a specified key in a dictionary
.update() - Updates the dictionary with a key value pair (can also update the dictionary using patient_1['height']=['165 cm'])
.values - Returns a list of the values in a dctionary

patient_1.setdefault('name')
patient_2.items()
patient_2.popitem()




"""Tuples"""

#Definition: Tuples are a data structure that contains a collection of elements. These elements are immutable and ordered.
#Tuples contain duplicates

cars=('BMW', 'Ford', 'Mercedes', 'Volkswagen', 'BMW')

# Tuple Methods
.count() - Counts the number of times a specified element occurs in a tuple.
.index() - Finds the specified element in a tuple and returns its position.

cars.count('BMW')
cars.index('Ford')



"""Lists"""

# Definition: Lists  are a data structure that contain a collection of elements.
# Lists are mutable and ordered, and contain duplicates.

fabric=['fur', 'velvet', 'cotton', 'linen', 'fur']

# List Methods
.append() - Adds an element at the end of a list
.pop() - Removes the last element of a list
.clear() - Clears all the elements of a list
.index() - Finds the specified value and returns its position in a list
list[0] - Returns the value in the specifed index
.count() - Returns the number of times a specified element is duplicated.
.extend() - Adds the end of a list to the end of a current list.
.insert() - adds an element a specifed position in a list
.remove() - Removes a specified element from a list.
.reverse() - Reverse the order of the list
.sort() - Sorts the list in alphabeltical order

fabric.sort()
fabric.insert(1, 'leather')
print(fabric.count('fur'))
