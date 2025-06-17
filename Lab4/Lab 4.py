import math
from datetime import datetime, timedelta
#Subtract five days from the current date
today = datetime.now()
five = today - timedelta(days=5)

print("Today date:", today)
print("Five days ago:", five)

#Write a Python program to print yesterday, today, tomorrow.
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.date())
print("Today:", today.date())
print("Tomorrow:", tomorrow.date())


#Write a Python program to drop microseconds from datetime.
now = datetime.now()
no_ms = now.replace(microsecond=0)

print("Datetime:", now)
print("Without microseconds:", no_ms)

##Write a Python program to calculate two date difference in seconds.
date1 = datetime(2025, 9, 23, 12, 0, 0)
date2 = datetime(2025, 9, 16, 9, 30, 0)

difference = date1 - date2
seconds = difference.total_seconds()

print("Difference in seconds:", seconds)

#Create a generator that generates the squares of numbers up to some number N.
def square_generator(n):
    for i in range(n + 1):
        yield i * i

for square in square_generator(5):
    print(square)

#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))
evens = even_generator(n)
print(",".join(map(str, evens)))

#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number: "))
for num in divisible_by_3_and_4(n):
    print(num)

#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

for val in squares(3, 7):
    print(val)

#Implement a generator that returns all numbers from (n) down to 0.
def countdown(n):
    for i in range(n, -1, -1):
        yield i

for num in countdown(5):
    print(num)
"""Write a Python program to convert degree to radian.
Input degree: 15
Output radian: 0.261904"""
d = 15
r = math.radians(d)

print("Input degree:", d)
print("Output radian:", round(r, 6))  

"""Write a Python program to calculate the area of a trapezoid.
Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5"""
h = 5
b1 = 5
b2 = 6

area = 0.5 * (b1 + b2) * h

print("Area of trapezoid:", area) 

"""Write a Python program to calculate the area of regular polygon.
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625"""
num= 4
len= 25

area = (num * len**2) / (4 * math.tan(math.pi / num))

print("Area of polygon:", round(area, 2)) 

"""Write a Python program to calculate the area of a parallelogram.
Length of base: 5
Height of parallelogram: 6
Expected Output: 30.0"""
b = 5
h = 6

area = b * h

print("Area of parrallelogram:", float(area))  



