"""
we don’t create any functions ourselves ,so import can load from function library to introduce function that already established

use below statement to include a module first!:
import [function library]

※Some modules have to install, I will prepare a separate briefing on this topic in future.
"""
import random
n = input()
if n == "I want to play this":
    print(random.randint(1,87))
else:
    pass

"""
Use below statement to give module a Alias:
import [function library] as [Customize name]
"""
import random as x
n = input()
if n == "I want to play this" and n != "?":
    print(x.randint(1,87))
else:
    if n == "?":
        print("don't be confuse😒")
    pass


"""
from [function library] import [function/class /variable]
"""
from random import randint
n = input()
if n == "I want to play this" and n != "?":
    print(randint(1,87))
else:
    if n == "?":
        print("don't be confuse😒")


"""
from [function library] import [function/class /variable] as [Customize name]
"""
from random import randint as x
n = input()
if n == "I want to play this" and n != "?":
    print(x(1,87))
else:
    if n == "?":
        print("don't be confuse😒")
