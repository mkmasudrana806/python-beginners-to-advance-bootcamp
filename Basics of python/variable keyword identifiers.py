"""
Variable: variable help us to store the value
"""
a = 2
print(a)

b = 3.5
print(b) 

c = "Hello World"
print(c)

d = True
print(d)

e = None
print(e)

name = "Masud Rana"
print('Welcome back, ', name, '!')

a = 5
b = 10
print(a+b)

# dynamic typing, means no need to mention data type
a = 7 # int


# static typing ( mainly used in c, c++, java)
# int number = 10

# dynamic binding, means we can assign any value to a single variable
x = 10
print(x)

x = "Masud"
print(x)

a = 5
b = 10
c = 15
print(a, b, c)

#instead we can do in single line
a, b, c = 5, 10, 15
print(a, b, c)

a = 5
b = 5
c = 5
print(a, b, c)

# instead do below
a = b = c = 5
print(a, b, c)


"""
keywords: keywords help us to compile our program
"""
# 39 keywords. keywords help us to compile our program

import keyword
print(keyword.kwlist)
"""
False	await	else	import	pass
None	break	except	in	raise
True	class	finally	is	return
and	continue	for	lambda	try
as	def	from	nonlocal	while
assert	del	global	not	with
"""
name = "masud"



"""
Identifiers: identifiers is the way of declaring variable
"""
# identifiers means the way of declaring variable
name = "masud rana"
num = 10

# there are some restriction to declare identifiers

# you can not start with digit
# 10num = 10 # not allowed

# you can not start with any special character except underscore(_)
# $digit = 103 #not allowed

_name = "masud rana"; #allowed
print(_name)

age_ = 23 #allowed
print(age_)
