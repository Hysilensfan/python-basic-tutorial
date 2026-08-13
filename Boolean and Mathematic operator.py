"""
As the common as daily, we using mathematic operating when do some expressions.
Fro example:
Today, I wanna know that 8 ÷ 2
so, you'll think about:
Take 8 as the dividend and 2 as the divisor. 8 is divisible by 2, with a quotient of 4 and a remainder of 0.

Mathematic operator will involves calculations like these!

Mathematic operator|In daily|Explains
+                  | +      |addition
-                  | -      |subtraction
*                  | x      |multiplication
/                  | ÷      |normal division has remainder
//                 | |      | divisibility no remainder
%                  | mod    |modulo division
**                 | ^      |exponentiation
"""
print(15 + 2)      # addition: calculate 15 + 2 and print result
print(15 - 2)      # subtraction: calculate 15 - 2 and print result
print(15 / 2)      # Division: calculate 15 ÷ 2 (float Division)
print(15 // 2)     # Divisible: quotient of 15 Divisible by 2
print(15 % 2)      # remainder: remainder of 15 divided by 2
print(15 ** 2)     # exponentiation: 15 squared

"""
Boolean:
Boolean or call it bool
It a TF(True or False) Value, and it can stand for a condition Whether it is valid or not.
"""
temp: bool = True            # bool value: define c is True
print(type(temp).__name__)  # c should return a boolean in theory
print(1 == True)  # In Computing, 1 is True;0 is False
print(0 == False)

# Boolean in conditional statement
if 999:  # >= 1 stand for True in condition statement
    print("Guga")

# Logical NOT returns the opposite boolean value.
if not 0:  # NOT False -> True
    print("Guga")
