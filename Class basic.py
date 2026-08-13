"""
Class
=====

A class is a blueprint for creating objects.
It can contain attributes (data) and methods (functions).

Basic syntax:

class ClassName:
    def __init__(self, parameters):
        self.attribute = value

    def method(self):
        statements


Object
======

An object is an instance of a class.

Example:

object_name = ClassName()


self
====

`self` refers to the current object.

It is used to access the object's attributes and methods.

For example:

self.name
self.age


__init__()
==========

`__init__()` is a special method that is automatically called
when an object is created.

It is commonly used to initialize the object's attributes.


Attributes
==========

Attributes are variables that belong to an object.

Example:

self.name = "Archer"
self.alive = False


Methods
=======

Methods are functions defined inside a class.

They can access and modify the object's attributes through `self`.

Example:

def attack(self):
    print(self.weapon)


Class vs. Function
==================

A function can perform a specific task.

A class can combine related data and functions into a single object.

Function:

    add(i, j)

Class:

    Multiplicationtable

    ├── Attributes
    │   ├── staringvalueI
    │   ├── staringvalueII
    │   └── result
    │
    └── Method
        └── add()


The class approach is useful when the data and operations
belong together and the object's state needs to be maintained.
"""


# ============================================================
# ex1: Using a class to create a multiplication table
# ============================================================

class Multiplicationtable(object):
    def __init__(self):
        self.staringvalueI = 1
        self.staringvalueII = 1
        self.result = 0

    def add(self):
        self.result = self.staringvalueI * self.staringvalueII
        print(
            " ".join(
                f"{self.staringvalueI}*{self.staringvalueII}={self.result}"
            ),
            end="  "
        )


mt = Multiplicationtable()

print("There is the multiplication table:")

for _ in range(9):
    for _ in range(9):
        mt.add()
        mt.staringvalueII += 1

    print()
    mt.staringvalueII = 1
    mt.staringvalueI += 1


# ============================================================
# ex2: Using a class to represent an Archer
# ============================================================

class Archer:
    def __init__(self):
        self.bone = "sword"
        self.body = "steel"
        self.blood = "fire"
        self.blades_created = 1000
        self.alive = False
        self.dead = False

    def unlimited_blade_works(self):
        print(f"I am the bone of my {self.bone}.")
        print(f"{self.body} is my body, and {self.blood} is my blood.")
        print(f"I have created over {self.blades_created} blades.")
        print(
            "Unknown to Death, Nor known to Life"
            if not self.alive and not self.dead
            else ""
        )
        print("As I pray...")
        print("Unlimited Blade Works!")


archer = Archer()
archer.unlimited_blade_works()
