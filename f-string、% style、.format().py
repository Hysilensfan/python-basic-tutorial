a = 1919810
print(f"the value of a is {a} , and its type is {type(a).__name__}")  # the f - string is modern python standard
print("the value of a is %d , and its type is" % a, type(a).__name__)  # % is legacy C-style approach
print("the value of a is {0} , and its type is {1}".format(a, type(a).__name__))  # .format() is transitional style
