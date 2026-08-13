"""
Dictionary:
A data structure that To achieve the hash table.
It has insertion-ordered
About data(key to value) sorting is in-order after V3.7.

It are indexed by below:
1.Range of numbers
2. Keys
Which can be any immutable type
Strings and numbers can always be keys
If a tuple contains any mutable object either directly or indirectly, it cannot be used as a key.

It is:
□ Changeable
□ Duplicates Not Allowed

dict() function:
can accept an iterable, where each element must be a pair of two elements
tuples are simply the most common representation

Data source:
https://docs.python.org/zh-tw/3.6/tutorial/datastructures.html
https://www.w3schools.com/python/
"""
dict_: dict = dict([(15, [1, 2]), (2, [3, 4])])
print(dict_)

"""
You can also using '{}' to create a dictionary.

Warning:
Must needs a pair of Key to value, the ':' character is between both.
"""
dict_: dict = {15: [1, 2], 2: [3, 4], 12: [5, 6]}
print(f"dict_'s all keys:\n{dict_.keys()}")
print(f"dict_'s all values:\n{dict_.values()}")
print(f"To get the dict_'s all pair of key to value:\n{dict_.items()}")
print(f"To get the dict_'s key 2 corresponding value:\n{dict_.get(2)}", end='\n\n')

dict_.update({15: [8, 7]})
print(f"Replace key 15 corresponding value:\n{dict_}")
dict2_: dict = dict_.copy()  # Or by using dict(dict_)
print(f"Got dict2_ via shallow copies the dict_:\n{dict2_}", end='\n\n')

print("Traversing the dictionary:")
for x, y in dict_.items():
    print(x, y)
print()

dict2_.popitem()
print(f"Deleted last element:\n{dict2_}")
dict_.pop(15)
print(f"Deleted the key corresponding value:\n{dict_}", end='\n\n')

del dict2_
print("Deleted the dictionary named dict2_")
try:
    print(dict2_)  # Raising NameError!
except NameError as n:
    print(f"I captured the {n}\n")  # But I capture and cease the error appearing.


"""
setdefault() method returns the value of the item with the specified key.
If the key does not exist, insert the key, with the specified value, see example below
"""
x: int = dict_.setdefault(12, 67)
print(f"key 12  corresponding value is:\n{x}")
dict_.setdefault(6, [99, 100])  # Added a pair that key is 6, value is [99, 100].
print(f"If the key does not exist, add it to the dictionary:\n{dict_}\n")

dict_.clear()
print(f"Cleared the dict_:\n{dict_}\n")

dict_reference: tuple = (chr(65), chr(66), chr(97))
dict3_: dict = dict.fromkeys(dict_reference, 67)
print(f"Create dict3_ via dict.fromkeys():\n{dict3_}")

