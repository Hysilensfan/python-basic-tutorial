"""
Shift Operators:
Left shift:
Shift the binary bits to the left, filling the right with 0s and discarding the leftmost bits.

Right shift:
Shift the binary digits to the right, filling the left with the sign bit and discarding the digits on the right.

source of data above:https://ithelp.ithome.com.tw/m/articles/10271689
"""
print(~binary & 0b11111)  # Mask
print(int("00101", 2))
print(bin(~binary & 0b11111))

a: int = 10
print(a, bin(a), sep='\n')
print(a << 1, bin(a << 1), sep='\n')  # 00001010 after bitwise left shift -> 00010100


b: int = 100
print(b, bin(b), sep='\n')
print(b >> 4, bin(b >> 4), sep='\n')  # 01100100 after bitwise right shift -> 00000110

"""
Bitwise NOT、AND、OR and XOR:
Python using two's complement to process nagative numbers
~ means signed binary complement.
So, ~n equal -(n + 1)

XOR:
1 if digits are different, else 0

AND:
1 if both digits are 1, else 0

OR:
1 if any digit is 1, else 0
"""
binary: int = 0b11010
print(~binary)  # -(26 + 1)
print(int("11010", 2))
print(bin(~binary))

print(0b10001 ^ 0b10)


print(bin(0b10001 ^ 0b10))  # Confirm XOR result(convert to binary)


print(0b10001 & 0b01)


print(bin(0b10001 & 0b01))  # Confirm AND result(convert to binary)


print(0b10001 | 0b0)

print(bin(0b10001|0b0)) # Confirm OR result(convert to binary)


# Base2 and Base 16
def decimal_to_binary(y: int) -> str:  # be like this function
    t, s = y, "0b"
    while t > 0:
        s += str(t % 2)
        t //= 2
    return s[:2] + s[2:][::-1]


print(bin(int(input())))  # convert decimal to binary
print(decimal_to_binary(int(input())))

def binary_to_decimal(e: int) -> int:  # be like this function
    d, r = list(map(int, str(e).replace("0b", ""))), 0
    for c in d:
        r = (r << 1) + c
    return r

print(int(input(), 2))  # convert binary to decimal
print(binary_to_decimal(int(input())))

def decimal_to_hexadecimal(w: int) -> str:  # be like this function
    table = "0123456789ABCDEF"
    t, s = w, "0x"
    while t > 0:
        s += table[t % 16]
        t //= 16
    return s[:2] + s[2:][::-1]


print(hex(int(input())))  # convert decimal to hex
print(decimal_to_hexadecimal(int(input())))

def hexadecimal_to_decimal(l):  # be like this function
    d, r = l.replace("0x", ""), 0
    for c in d:
        v = int(c) if c.isdigit() else ord(c) - ord('A') + 10
        r = (r << 4) + v
    return r

print(int(input(), 16))  # convert hex to decimal
print(hexadecimal_to_decimal(int(input())))
