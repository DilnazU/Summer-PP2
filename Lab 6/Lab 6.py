import time
import math

#Write a Python program with builtin function to multiply all the numbers in a list
from functools import reduce

def task1(x):
    return reduce(lambda x, y: x * y, x)
x = [23, 33, 43]
print("Product:", task1(x))

#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def task2(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)
task2("Programming Principles")

#Write a Python program with builtin function that checks whether a passed string is palindrome or not
def task3(s):
    return s == s[::-1]
print("String is palindrome:", task3("python"))
print("String is palindrome:", task3("pp2"))

#Write a Python program that invoke square root function after specific milliseconds.
x=int(input("Введите цифру:"))
y=int(input("Введите цифру:"))
def task4(x, y):
    time.sleep(y / 1000)
    res = math.sqrt(x)
    print(f"Square root of {x} after {y} milliseconds is {res}")
task4(x,y)

#Write a Python program with builtin function that returns True if all elements of the tuple are true
def task5(x):
    return all(x)
print("All true:", task5((True, 1, "text")))
print("All true:", task5((True, 0, "text")))  
