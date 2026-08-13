"""
Basic IO(Input and Output):
input() function:
Read a string from user input (stops at newline by default).
Normal situation, this function will return string

print() function:
print(variable, sep=' ', end='\n')
Default:
□  sep(separator) is a half-width space(' ')
□  end(end character) is a newline('\n')
"""
s = input()
print(type(s))  # To check a object's type, so this statement would print:<class 'str'>
print(type(s).__name__)  # Because __name__ will return a attribute's name, so this statement would print:str

print(1, 2, 3, 4, 5, sep=" ", end="\n")  # default behavior: elements separated by space and end with newline
print(1, 2, 3, 4, 5, sep="")  # no separator between elements
print(1, 2, 3, 4, 5, sep=" ", end="")  # no newline at the end of output

"""
int() function:
Python int has no fixed size limit like C
This function will converts object into an integer
"""
d = int(input())
print(type(d).__name__)  # This statement would print:int

"""
float() function:
This function will converts object into float
"""
d = float(input())
print(type(d).__name__)  # This statement would print:float
