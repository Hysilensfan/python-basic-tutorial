"""
List:
Lists are used to store multiple items in a single variable.

Lists are created using square brackets('[' and ']')
also can create via list() function

List Items
□ ordered
□ changeable
□ indexed
□ allow duplicate values

Data source:https://www.w3schools.com/python/
"""
# Access items
from typing import List

test: List[int] = [1, 2, 3, 4]  # This action named packing
"""
index  |[0]|[1]|[2]|[3]
element| 1 | 2 | 3 | 4
"""
test2: List[int] = list(range(6, 18))  # list(Traversable data structure)
print(f"test:\n{test}\ntest2:\n{test2}\n")

print(f"test2's index 0 element:\n{test2[0]}")
print(f"test2's index 2 ~ 12 element:\n{test2[2:13]}\n")  # Like:[print(test[x]) for x in range(2, 13)]

# Changing list
test2[1] = 3
print(f"Replace index 1 element:\n{test2}")
test2[4:9] = [19, 20, 21, 22]
print(f"Replace index 4 ~ 9 element:\n{test2}")

# Add elements
test2.append(18)  # Append to back of the list
print(f"test2:\n{test2}")
test2.insert(2, 4)  # Append to back of index 1(index 2) of the list
print(f"test2:\n{test2}")
test.extend(test2)  # Add the elements of tropical to thislist, like:test += test2 or [test.append(x) for x in test2]
print(f"test2:\n{test}")

# Remove element
test.remove(3)  # Remove the element 3 that first appeared in this list.
print(f"test2:\n{test}")
test.pop(3)  # Remove the index 3 element in test, parameter default -1
print(f"test2:\n{test}\n")
test2.clear()
print(f"Clear all elements about test2:\n{test2}\n")
del test2

try:
    print(test2)
except NameError as n:
    print(f"I Captured {n}\n")

# Loop list
for index in range(len(test)):  # index based-for
    print(test[index])
for element in test:  # range based-for
    print(element)

# Sorting
test3: List[int] = test.copy()  # Like test[:]
print(f"I copied test to create test3:\n{test3}\n")
test3.sort()  # Default reverse is False
print(f"Sorted test3:\n{test3}")
test3.sort(reverse=True)
print(f"Sorting and reverse it:\n{test3}")
test3.reverse()  # Like:test3[::-1]
print(f"Reverse it via reverse() function:\n{test3}")
print(f"Sorting and generate new thing then reverse sequence:\n{sorted(test3, reverse=True)}\n")  # .sort() Only accept list, but sorted accept any iterables.

# counting elements number
print(f"To count how many times 4 appears in this sequence:\n{test3.count(4)}")
""""
In fact using collections.Counter() is better and makes it easier to know whick key-value pairs do you need.
"""

"""
Tuple:
THIS STRUCTURE IS HOW LIKE LIST!!!
□ Unchangeable:cannot change, add or remove items after the tuple has been created.

Access:
Like list
Change:
Unchangeable!
Update:
using tuple() to convert list's data structure, before do it changing element.
Join:
Like list
Loop:
Like list
"""
# unpack tuples
(a, b, c) = ("0x65", "0x66", "0x67")  # Unpacking and assign value
print(a, b, c)

"""
Set:
□ Unordered:
Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
□ Unchangeable:
Set items are unchangeable, meaning that we cannot change the items after the set has been created.
□ Duplicates Not Allowed:
Sets cannot have two items with the same value.

Create:
Using curly braket('{' and '}') to create a set.
Or by using set() function.

Change:
Unchangeable!
Join:
Like list
Loop:
Like list
"""

s: set = set([False, 0, True, 1])  # False 、 0 regarded as same object in set.and True 、 1 too.
print(s)

sets: set = {"w", "A", "B", "Z", "F", "q", "t", "x", "Y"}
sets2: set = {"y", "X", "T", "Q", "f", "z", "b", "a", "W"}
print(f"sets now:\n{sets}\n")

# Add element
sets.add("b")
print(f"sets now:\n{sets}\n")

# Update set
sets.update(sets2)
print(f"sets now:\n{sets}\n")

# Remove
try:
    sets.remove("g")
except KeyError as k:
    print("remove() function will raise error!")

sets.discard("g")
print("discard() function will not raise error!\n")
"""
Else operation like copy()、pop()、clear()、del...
Above operation be like list, No any specifics.
"""

# Comparing
sets3: set = {3, 2, 8, 9, 'A'}
sets4: set = {2, 7, 9, 'B'}
print(sets3.difference(sets4))  # A - B -> 8、3、'A'
print(sets3.intersection(sets4))  # A & B -> 9、2
print(sets3.union(sets4))  # A | B -> 2、3、'A'、7、8、9、'B'
print(sets3.symmetric_difference(sets4))  # A ^ B -> 3、'A'、7、8、'B'

"""
Frozen set:
HOW BELIKE SET, BUT IT'S CANNOT ADD OR REMOVE...

"""
sets5: frozenset = frozenset(sets2)
print(sets5)

