# If
# If the number is positive, we print an appropriate message

num = -2
if num > 0:
    print(num, "is a positive number.")
    
print("This is always printed.")

if num>0:
    print(num, "is a positive number")
    
num=5



num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")


# If else:
num = 0

if (num >= 0):
    print("Positive or Zero")
else:
    print("Negative number")

if (num>=0):
    print("Positive or zero")
else:
    print("Negative")

## Define a function with conditional statement

(max_num(400,60,1150))

def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3

max_num(80,41,3)
(max_num(400,60,1150))


# Nested If
num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

############# Loops #####################
# for Loop
# for each item in sequence , last item reached , no - body of loop , yes , exit loop


#Ex:1

snacks = ['pizza','burger','shawarma','franky']

for x in snacks:
    print(x, "is a yummy snack")
    #print("Also try", snacks[x+1])

print("Good day!")


#Ex:2

num = int(input("Please give a number: "))

factorial =1
if num < 0:
    print("Number must be positive")
elif num == 0:
    print("factorial = 1")
else:
    for i in range(1,num+1):       #(If user gives input of 5, range will have the values [1,2,3,4,5], only if we give the upper limit in the range as num+1, i.e.6 in this case)
        factorial = factorial * i   #range has now the values [1,2,3,4,5]
        print(factorial)
    print("factorial =  " ,factorial)

#What is a factorial?
#5*4*3*2*1
#7*6*5*4*3*2*1

x = range(5)
for i in x:
    print(i)
help(range)

#Nested for loop

for i in range(0,3):
    for j in range(0,3):
        print(i,j)

# For loop with else:
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")


########################## While Loop #############################
# Program to add natural
# Enter the loop , test expression , true , body of code , if false - exit loop.
# numbers upto
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

n = 4

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter
    print("sum:", sum)
    print("i:" , i)

# print the sum
print("The sum is", sum)


a=int(input("Please give a natural number: "))
b=list(range(1,a+1)) 
print(b)
# initialize sum and counter
sum = 0
while sum<b[-1]:
    for m in b:
        sum=sum+m
        print("sum:", sum)
    
# print the sum
print("The sum is", sum)   


b=[1,2,3,4,5,7]
# initialize sum and counter
sum = 0
while sum<b[-1]:
    for m in b:
        sum=sum+m
        print("sum:", sum)
    
# print the sum
print("The sum is", sum)   

c=['a','v','n','i','s','h']
c

for i in c:
    print(i,end='')

# While loop with else
# Example to illustrate
# the use of else statement
# with the while loop

counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")



#Ex: 1

count = 0

while count < 20:
    print("Digit: ", count)
    count = count + 1

print("Thank you")

#Ex: 2

import random

n = 5

random_number = int(n * random.random())

guess = 25

while guess != random_number:
    guess = int(input("New Number: "))
    if guess > 0:
        if guess > random_number:
            print("number is too large")
        elif guess < random_number:
            print("number is too small")
    else:
        print("sorry that you are giveup!")
        break
else:
    print("Congratulations. YOU WON!")


################### Modules#################################
#Ex:1

import math

x = 16
math.sqrt(x)

math.pow(2,5)


#Ex:2

import calendar

cal = calendar.month(2020,2)

print(cal)

calendar.isleap(2018)

calendar.isleap(2021)

dir(calendar)

