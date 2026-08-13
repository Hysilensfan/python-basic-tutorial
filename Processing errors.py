# if there's an error it will be ignored(no output)
try:
    a, b =map(int,input().split())
    print(a // b)
except EOFError:
    pass


a,b = map(int,input().split())
print(a // b)
"""
In the code above:
If b is 0, a ZeroDivisionError will occur because
division by zero is not allowed.

The terminal will display:
ZeroDivisionError: integer division or modulo by zero
"""


# using raise to report error by selves
a,b = map(int,input().split())
print(a//b)
raise ZeroDivisionError("Hah ha u the fool😏")


try:
    a,b=map(int,input().split())
    print(a//b)
except Exception as e:  # It can be used in try/except blocks to catch problems in the program
    print(f"the {str(e)} error is appeared,fuck off!")
