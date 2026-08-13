"""
To define a function:

def [function_name](parameters):
    statements
    return value

default return None
"""
# Define multiplication table function
def add(i,j):
    result = i * j
    print(" ".join(f"{i} x {j} = {result}"), end="  ")
print(f"there are the multiplication table: ")
for index in range(81):
    i, j = index // 9 + 1 ,index % 9 + 1
    add(i, j)
    while j == 9:
        print()
        break

# The code below does the same thing as the code above.
add = lambda i,j:print(" ".join(f"{i} x {j} = {i * j}"), end="  ")
print(f"there are the multiplication table: ")
for index in range(81):
    i, j = index // 9 + 1 ,index % 9 + 1;add(i, j)
    while j == 9:
        print()
        break

"""
To define a lambda function:

[function_name] = lambda parameter:statements

Warning:
A lambda function will automation return the expressions value, so you're not nassaccery write the return statement.
"""

c = lambda d:d - 4 # Here c is a lambda function, which is like a tiny function we write in one line. It returns d minus 4
def C(d): # Here c is a normal function. It does the same thing: subtract 4. But it’s written in multiple lines and has a name r inside
    r = d - 4
    return r


d: int = int(input())
print(c(d))

e: int = int(input())
print(C(e))

c = lambda a,b:a  *b # Lambda can take more than one input. Here a and b are multiplied and returned


print(c(*map(int, input().split())))

d = lambda a, b, c:b ** 2 - 4 * a * c # Here lambda returns b² - 4ac


print(d(*map(int, input().split())))

"""
Type hints
Features introduced starting with Python 3.5.
The Python runtime does not enforce function and variable type annotations. They can be used by third party tools such as type checkers, IDEs, linters, etc.
While type hints can be simple classes like float or str, they can also be more complex. The typing module provides a vocabulary of more advanced type hints.

Usage:
def [function_name](parameter1: class, parameter2: class, ...) -> [return value's class]:
    statements
    return value

Surmise the actual return type differs from the Type hints, some compilers will display a message in the Problems field similar:
"Expected type '[hint_returntype]', got '[pratical_returntype]' instead."

Source of data:https://docs.python.org/3.14/library/typing.html
"""

def ex(a: int, b: int, c: int) -> float:  # This example demonstrates the use of type hints.
    s: int = (a + b + c) // 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


print(ex(*map(int, input().split())))
