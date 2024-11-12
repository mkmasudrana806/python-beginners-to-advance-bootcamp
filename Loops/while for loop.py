"""
# Loops in python
There are two type of loop in python
1.  while
2.  for
break, continue, else statement with while loop
"""

# while loop
i = 0
while i < 10:
    print(i)
    i += 1


# break statement
print("while loop with break")
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# continue statement
i = 1
print("while loop with continue")
while i < 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1


# while whit else
i = 1
while i<5:
  print(i)
  i+=1
else:
  print("i is no longer less than 5")
  

# guessing game
import random

to_be_guessed = int(random.randint(0, 100))
guess = 0
while guess != to_be_guessed:
    guess = int(input("Enter your guessing number: "))
    if guess > to_be_guessed:
        print("Number too large")
    elif guess < to_be_guessed:
        print("Number too small")
else:
    print("Congratulations. You made it!")



# loop in list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# loop in tuple
fruits = ('apple', 'banana', 'cherry')
for fruit in fruits:
    print(fruit)

# loop in set
fruits = {'apple', 'banana', 'cherry'}
for fruit in fruits:
    print(fruit)

# loop in string
name = "Masud Rana"
for char in name:
    print(char)

# loop with break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break



# print 1 to 10 numbers
for i in range(1, 11):
  print(i)
else:
  print("Loop finished!") # it will be printed else with for loop. it will be executed when loop is finished

# Note: else block not work if loop terminate with break statement
for i in range(1, 5):
  if i == 3: break
  print(i)
else:
  print("Loop finished!") # it will not be printed


# for loop with pass statement. loop will not do anything
for i in 1, 2, 3, 4:
  pass # without pass, it throw an erro

# nested for loop to print 25 uniques pair
for i in range(1, 6):
  for j in range(1, 6):
    print(i, j)


# pattern printing
"""
*
**
***
****
*****
"""

row = int(input("Enter number of row: "))
for i in range(1, row+1):
  for j in range(i):
    print("* ", end="")
  print("\n")