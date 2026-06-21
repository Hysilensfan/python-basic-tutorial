s = input()  # read a string from user input (stops at newline by default)
print(type(s).__name__)  # default type is string (str)

s = int(input())  # int() converts input string into an integer
# Python int has no fixed size limit like C

print(type(s).__name__)  # we can convert types using built-in functions

n = [1, 2, 3, 4, 5]  # create a list named n

print(*n, sep=" ", end="\n")  # default behavior: elements separated by space and end with newline

print(*n, sep="")  # no separator between elements

print(*n, sep=" ", end="")  # no newline at the end of output
