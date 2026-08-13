# if there's an error it will be ignored(no output)
try:
    a,b=map(int,input().split())
    print(a//b)
except EOFError:
    pass


#if an error occurs,for example dividing by zero
a,b=map(int,input().split())
print(a//b)
#terminal will show:
#ZeroDivisionError: integer division or modulo by zero


#using raise to report error by selves
a,b=map(int,input().split())
print(a//b)
raise ZeroDivisionError("Hah ha u the fool😏")


try:
    a,b=map(int,input().split())
    print(a//b)
except Exception as e: # It can be used in try/except blocks to catch problems in the program
    print(f"the {str(e)} error is appeared,fuck off!")
