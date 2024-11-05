"""
there are two type of applications. static and dynamic. 
# in static application, no need to take input from user. like calender, clock
# in dynamic application, we need to take input from user. like youtube, facebook
"""

input() # it take input from user and print automatically

# Note: by default all the value passing to input() function  are converted to the 'str'
name = input()
type(name)  # str

age = input() # assume take number as input
type(age) # 'str'

# we need to type conversion of different 
age = int(age) # convert 'str' to 'int'
type(age) # int


# take name form user and give a message
name = input("Enter your name: ")
print("Welcome, ", name, "!")


# simple arithmatic addition, subtruction and multiplication 
# must convert str to integer like `num1 = int(input("Enter first number: "))`
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# or convert both num1,num2 variable into integer type
result1 = int(num1) + int(num2)
result2 = int(num1) - int(num2)
result3 = int(num1) * int(num2)
print("Additon of ", num1, "and", num2, "is", result1) 
print("Subtruction of ", num1, "and", num2, "is", result2)
print("Multiplication of ", num1, "and", num2, "is", result3)



"""
Type conversion in Python
# type conversion help us to convert any type of data into desired type Note: input() function take all the input as 'string'
"""

# implicit type conversion ( interpreter itself do it )
res = 10 + 20.5
type(res) # float

type(10 + 20) # int

type(2 + "2") # give error. because integer and string is not possible to addition

# instead we can do like
type( 2 + int("2")) # int
type( 2 + float("2")) # float

# integer convert
num = 34.5
num1 = int(num)  
print(num1) # 34


# flaot convert
num2 = 10
num3 = float(num2) 
print(num3) # 10.0


# Note: we can not convert complex to int or float type
complexNumber = 2 + 2j
intNumber = int(complexNumber) # int() argument must be a string, a bytes-like object or a real number, not 'complex'
floatNumber = float(complexNumber) # we don't do that


"""
# Literals
# whatever we store in variable is called literals
"""
# variable nothing but it is just a container, inside variable we can store any knind of value
a = 10 # a is the variable, = is the operator, 10 is the literal
 
# there are some literals

# binary literal
a = 0b1011 
print(a) # 10 in decimal
type(a) # int

# decimal literal
b = 100 
print(b) # 100 

# octal literal
c = 0o7 
print(c) # 7 in decimal

# hexidecimal literal
d = 0x12c 
print(d) # 300 in decimal

# float literal
f = 1.5

g = 6.63e23 # 6.63x10^23
print(g)
type(g) # type

# complex literal
x = 3.14j
print(x)
type(x) # complex

print(x.real) # print real part: 0.0
print(x.imag) # print imaginary part: 3.14 


# string literal
str1 = 'this is python' 
str2 = "this is python" 
#Note: we have to use three single or double quote to write multiline string
multiline_str = '''while writing multiline string, must use triple quotes''' 
str4 = """this is python""" 
unicode_str = u"\U001f600\U0001F606\U0001F923"
raw_str = r"raw \n string"
print(str1)
print(str2)
print(multiline_str)
print(str4)
print(unicode_str)

# boolean literal
# True = 1
# False = 0
a = True + 4 # 5
print(a)

b = False + 4
print(b) # 4

# None literal
a = None
print(a)

