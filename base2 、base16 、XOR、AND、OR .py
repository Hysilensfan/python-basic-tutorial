# another usage of int function
print(int(input(),2))  # convert binary to decimal

def decimal_to_binary(y):  # be like this function
    t, s = int(y), "0b"
    while t > 0:
        s += str(t % 2)
        t //= 2
    return s[:2] + s[2:][::-1]

print(int(input(),16))  # convert hex to decimal

def binary_to_decimal(e):  # be like this function
    d, r = list(map(int, e.replace("0b", ""))), 0
    for c in d:
        r = (r << 1) + c
    return r

print(bin(int(input())))  # convert decimal to binary

def decimal_to_hexadecimal(w):  # be like this function
    table = "0123456789ABCDEF"
    t, s = int(w), "0x"
    while t > 0:
        s += table[t % 16]
        t //= 16
    return s[:2] + s[2:][::-1]

print(hex(int(input())))  # convert decimal to hex

def hexadecimal_to_decimal(l):  # be like this function
    d, r = l.replace("0x", ""), 0
    for c in d:
        v = int(c) if c.isdigit() else ord(c) - ord('A') + 10
        r = (r << 4) + v
    return r

print(0b10001^0b10)  # XOR: 1 if digits are different, else 0


print(bin(0b10001^0b10))  # confirm XOR result(convert to binary)


print(0b10001&0b01)  # AND: 1 if both digits are 1, else 0


print(bin(0b10001&0b01))  # confirm AND result(convert to binary)


print(0b10001|0b0)  # OR: 1 if any digit is 1, else 0


print(bin(0b10001|0b0)) # confirm OR result(convert to binary)
