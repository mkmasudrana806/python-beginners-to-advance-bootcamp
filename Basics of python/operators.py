"""
Operator in python
1. Arithmetic Operators
2. Relational Operators or comparision operators
3. Assignment Operators
4. Logical Operators
5. Bitwise Operators
6. Assignment Operators
7. Membership Operators
"""

# Arithmetic Operatos are: +, -, *, /, %, **, =

#   + 
add = 10 + 20
print(add)

#   -
sub = 10 - 20
print(sub)

# *
mul = 10 * 20
print(mul)

# /
div = 10 / 20
print(div) # return quotient

# % 
a = 10
b = 3
remainder = a % b # return the remainder 
print(remainder)

# ** exponential operator
exp = 2 ** 3 # similar to:  2 * 2 * 2
print(exp)

# // floor division
a = 15
b = 2
ans = a // b
print(ans) # return floor value that is 7


"""
Relational Operators
"""
# Relational Operatos: <, >, <=, >=, ==, !=

a = 10
b = 20
if a > b:
  print("a is greater than b")
else:
  print("b is greater than a")

a = 10
b = 20
if a < b:
  print("a is less than b")
else:
  print("b is less than a")

a = 10
b = 20
if a <= b:
  print("a is less than or equal to b")
else:
  print("b is less than or equal to a")

a = 10
b = 20
if a >= b:
  print("a is greater than or equal to b")
else:
  print("b is greater than or equal to a")

a = 10
b = 20
if a == b:
  print("a is equal to b")
else:
  print("a is not equal to b")

a = 10
b = 20
if a != b:
  print("a is not equal to b")
else:
  print("a is equal to b")


"""
Aissgnment Operators
"""

# = (Assign)
x = 5
print("=", x)  # Output: 5

# += (Add and Assign)
x = 5
x += 3  # Same as x = x + 3
print("+=", x)  # Output: 8

# -= (Subtract and Assign)
x = 5
x -= 3  # Same as x = x - 3
print("-=", x)  # Output: 2

# *= (Multiply and Assign)
x = 5
x *= 3  # Same as x = x * 3
print("*=", x)  # Output: 15

# /= (Divide and Assign)
x = 5
x /= 3  # Same as x = x / 3
print("/=", x)  # Output: 1.666...

# %= (Modulus and Assign)
x = 5
x %= 3  # Same as x = x % 3
print("%=", x)  # Output: 2

# //= (Floor Divide and Assign)
x = 5
x //= 3  # Same as x = x // 3
print("//=", x)  # Output: 1

# **= (Exponent and Assign)
x = 5
x **= 3  # Same as x = x ** 3
print("**=", x)  # Output: 125

# &= (Bitwise AND and Assign)
x = 5  # (binary 0101)
x &= 3  # x = x & 3 (binary 0011)
print("&=", x)  # Output: 1

# |= (Bitwise OR and Assign)
x = 5  # (binary 0101)
x |= 3  # x = x | 3 (binary 0011)
print("|=", x)  # Output: 7

# ^= (Bitwise XOR and Assign)
x = 5  # (binary 0101)
x ^= 3  # x = x ^ 3 (binary 0011)
print("^=", x)  # Output: 6

# >>= (Bitwise Right Shift and Assign)
x = 5  # (binary 0101)
x >>= 1  # x = x >> 1 (shift right by 1)
print(">>=", x)  # Output: 2

# <<= (Bitwise Left Shift and Assign)
x = 5  # (binary 0101)
x <<= 1  # x = x << 1 (shift left by 1)
print("<<=", x)  # Output: 10

# := (Walrus Operator)
print(y := 3)  # Assigns 3 to y and prints 3
print("y =", y)  # Output: y = 3


"""
Logical Operators
"""

# logical and operator. execute statement if both conditions are true
if(5<10 and 2 > 1):
    print("yes condition true")

# logical or operator. execute statement if any of the conditions are true
if(5<10 or 2<1):
    print("yeah!, execute. one condition is true")

# logical not operator. return true if condition is false
print(not(5<10 and 2>1)) # Return true if condition is false





"""
Identity operator: is, is not
"""

# is: Returns True if both variables are the same object
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
z = x # here x and z are hold the same memory location. so x and z are equal

if(x is z):
  print("x is z")
else:
  print("x is not z")
 

# is not: Returns True if both variables are not the same object
if(x is y):
  print("x is y")
else:
  print("x is not y")
  
  



"""
Membership operator
"""
# Membership operators: in, not in

# in: Returns True if a sequence with the specified value is present in the object
x = [1, 2, 3, 4]
if(2 in x):
  print("2 is present in x")
else:
  print("2 is not present in x")

# not in: Returns True if a sequence with the specified value is not present in the object
if(5 not in x):
  a = 5 not in x # True
  print(a) # True
  print("5 is not present in x")
else:
  print("5 is present in x")




"""
Bitwise Operators
"""
# Variables to demonstrate bitwise operations
a = 10  # In binary: 1010
b = 4   # In binary: 0100

# & (Bitwise AND)
result_and = a & b  # 1010 & 0100 = 0000
print("& (AND):", result_and)  # Output: 0

# | (Bitwise OR)
result_or = a | b  # 1010 | 0100 = 1110
print("| (OR):", result_or)  # Output: 14

# ^ (Bitwise XOR)
result_xor = a ^ b  # 1010 ^ 0100 = 1110
print("^ (XOR):", result_xor)  # Output: 14

# ~ (Bitwise NOT)
result_not = ~a  # ~1010 = -(1010 + 1) = -11
print("~ (NOT):", result_not)  # Output: -11

# << (Left Shift)
result_left_shift = a << 1  # 1010 << 1 = 10100
print("<< (Left Shift):", result_left_shift)  # Output: 20

# >> (Right Shift)
result_right_shift = a >> 1  # 1010 >> 1 = 0101
print(">> (Right Shift):", result_right_shift)  # Output: 5




