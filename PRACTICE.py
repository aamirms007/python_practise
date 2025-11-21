'''name = "Aamir"
age = 25
msg = f"My name is {name} and my age is {age}"
print(msg)

def reverse_string(s):
    return s[::-1]

print(reverse_string("Python"))
# REVERSE BY FUNCTION

def reverse_string(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev

print(reverse_string("Hello"))

################## SLICING
nums = [10, 20, 30, 40, 50]

print(nums[1:4])   # [20, 30, 40]
print(nums[:3])    # [10, 20, 30]
print(nums[2:])    # [30, 40, 50]

##########mODIFY lIST

nums = [1, 2, 3]
nums[1] = 10
print(nums)   # [1, 10, 3]
###########sort and sorted

nums = [3,1,2]
nums.sort()
print(nums)  # [1,2,3]

nums = [3,1,2]
print(sorted(nums))  # [1,2,3]
print(nums)          # original list remains same

######### del () and len()

nums = [10,20,30]
del nums[1]     # deletes 20
print(len(nums)) # 2
########list

numbers = [10, 20, 30, 40, 50]

print(numbers[-1])   # 50  (last element)
print(numbers[-2])   # 40  (second last)
print(numbers[-3])   # 30

colors = ["red"]
colors.append("blue")
print(colors)

squares = [x*x for x in range(5)]
evens = [y for y in range(10) if y % 2 == 0]
ODD = [z for z in range(10) if z % 2 == 1]
print(squares)
print(evens)
print(ODD)
############ Tuple
my_tuple = (10, 20, 30)
t = (5,)    # valid tuple
t_1= 1, 2, 3
t_2 = ("aa",10,20)


print(type(my_tuple))
print(type(t))
print(type(t_1))
print(type(t_2))

###########for loops

for i in range(5):
    print(i)
colors = ["red", "green", "blue"]
for c in colors:
    print(c)
for ch in "Python":
    print(ch)
nums = [10, 20, 30]
total = 0
for n in nums:
    total += n
print(total)

i = 1
while i <= 5:
    print(i)
    i += 1


n = 5
while n > 0:
    print(n)
    n -= 1
i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print(total)

text = ""
while text != "exit":
    text = input("Enter text: ")

num = 10
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

marks = 45

if marks >= 40:
    print("Pass")
else:
    print("Fail")

marks = 85

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("Fail")

num = -5

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
# 5 Type Casting Examples in one Python program

# 1. String to Integer
x = "25"
y = int(x)
print("String to int:", y, type(y))

# 2. Float to Integer
a = 10.56
b = int(a)
print("Float to int:", b, type(b))

# 3. Integer to String
num = 100
text = str(num)
print("Int to string:", text, type(text))

# 4. Integer to Float
p = 15
q = float(p)
print("Int to float:", q, type(q))

# 5. List to Tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print("List to tuple:", my_tuple, type(my_tuple))

my_tuple = (10, 20, 30, 40)

# Convert tuple to list
my_list = list(my_tuple)

print(my_list)
print(type(my_list))

# Dictionary Examples (All in one program)

# 1. Create (define) a dictionary
student = {
    "name": "Aamir",
    "age": 20,
    "course": "Python"
}
print("Original dictionary:", student)

# 2. Access values using keys
print("Name:", student["name"])
print("Course:", student["course"])

# 3. Add a new key-value pair
student["city"] = "Mumbai"
print("After adding city:", student)

# 4. Modify (update) a value
student["age"] = 25
print("After updating age:", student)

# 5. Delete a key-value pair
del student["course"]
print("After deleting course:", student)

# 6. Get all keys and values
print("Keys:", student.keys())
print("Values:", student.values())

# Dictionary
student = {
    "name": "Aamir",
    "age": 20,
    "course": "Python"
}

# 1. Loop through keys
print("Keys:")
for key in student:
    print(key)

# 2. Loop through values
print("\nValues:")
for value in student.values():
    print(value)

# 3. Loop through key-value pairs
print("\nKey-Value pairs:")
for key, value in student.items():
    print(key, ":", value)

student = {
    "name": "Aamir",
    "marks": [85, 90, 78, 92]
}

# Read the whole list
print("Marks List:", student["marks"])

# Read single value
print("Math mark:", student["marks"][0])
print("Sci mark:", student["marks"][1])
print("hist mark:", student["marks"][2])
print("PE mark:", student["marks"][3])

# Loop through list inside dictionary
print("All marks:")
for m in student["marks"]:
    print(m)

d = {"name": "Aamir", "age": 25}

print(d.keys())
print(d.values())
print(d.items())

d.update({"city": "Mumbai"}) # add or modify
print(d.items())
print(d.get("age"))

student = {
    "name": "Aamir",
    "age": 20,
    "course": "Python"
}

print(student)
# 1. Modify using key
student["age"] = 25

# 2. Modify using update()
student.update({"name": "Aamir Khan"})

print(student)

def say_hello(name):
    print("Hello", name)

say_hello("Aamir")

def add(a, b):    # a, b → PARAMETERS
    print(a + b)

add(10, 20)       # 10, 20 → ARGUMENTS


def details(name, age):
    print(name, age)

details("Aamir", 25)

details(age=25, name="Aamir")

def greet(name="Guest"):
    print("Hello", name)

greet()             # Hello Guest
greet("Aamir")      # Hello Aamir

def total(*nums):
    return sum(nums)

print(total(1,2,3,4))

def total(*nums):
    return sum(nums)

print(total(1,2,3,4))


import csv

def read_csv_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

# Call the function with full path
read_csv_file("E:/DevOps/Data_analytics_by_fayaz/mock_pract/PYTHON/QUERY.csv")

import json

def read_json_file(filename):
    # Open the JSON file
    with open(filename, 'r') as file:
        # Load the JSON content
        data = json.load(file)

        # Print the entire JSON data
        print("JSON Data:")
        print(data)


# Call the function with file path
read_json_file("E:/DevOps/Data_analytics_by_fayaz/mock_pract/PYTHON/data.json")

class Student:
    # Constructor to initialize data
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    # Method 1: Show student details
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll}")
        print(f"Marks: {self.marks}")

    # Method 2: Check pass/fail
    def check_result(self):
        if self.marks >= 40:
            print(f"{self.name} has PASSED.")
        else:
            print(f"{self.name} has FAILED.")
# Creating objects (students)
s1 = Student("Aamir", 101, 85)
s2 = Student("Mahi", 102, 32)

# Calling methods
s1.show_details()
s1.check_result()

s2.show_details()
s2.check_result()


class Calculator:

    # Method 1: Constructor
    def __init__(self):
        print("Calculator Ready!")

    # Method 2: Addition
    def add(self, a, b):
        return a + b

    # Method 3: Subtraction
    def subtract(self, a, b):
        return a - b

    # Method 4: Multiplication
    def multiply(self, a, b):
        return a * b

    # Method 5: Division
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

    # Method 6: Square of a number
    def square(self, a):
        return a * a


# Creating object
calc = Calculator()

# Using methods
print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.subtract(10, 5))
print("Multiplication:", calc.multiply(10, 5))
print("Division:", calc.divide(10, 5))
print("Square:", calc.square(7))


# Parent Class
class Vehicle:
    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is stopping")


# Child Class (inherits Vehicle)
class Car(Vehicle):
    def open_doors(self):
        print("Car doors are opened")


# Grandchild Class (inherits Car)
class ElectricCar(Car):
    def charge_battery(self):
        print("Electric car is charging")


# Creating objects
v = Vehicle()
c = Car()
e = ElectricCar()

# Calling methods
print("=== Vehicle ===")
v.start()
v.stop()

print("\n=== Car ===")
c.start()  # inherited from Vehicle
c.open_doors()  # Car’s own method
c.stop()  # inherited

print("\n=== Electric Car ===")
e.start()  # from Vehicle
e.open_doors()  # from Car
e.charge_battery()  # own method
e.stop()  # from Vehicle


class Bird:
    def fly(self):
        print("Bird flies in the sky using wings")

class Aeroplane:
    def fly(self):
        print("Aeroplane flies using engines")

class Superman:
    def fly(self):
        print("Superman flies using superpowers")


# Using polymorphism
for obj in (Bird(), Aeroplane(), Superman()):
    obj.fly()

from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


# Child Class 1
class Car(Vehicle):
    def start(self):
        print("Car starts with a key")


# Child Class 2
class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start button")


# Using the child classes
car = Car()
bike = Bike()

car.start()
bike.start()

def numbers():
    for i in range(1, 5):
        yield i

gen = numbers()
for num in gen:
    print(num)

def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for num in even_numbers(10):
    print(num)


def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

import io

data = io.StringIO("Hello Python")
print(data.read())

# my_module.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def greet(name):
    return f"Hello, {name}!"
import my_mod

result = my_mod.add(10, 20)
print("Addition Result:", result)


try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid number!")
finally:
    print("Program finished.")
try:
    x = -1
    if x < 0:
        raise Exception("Negative numbers not allowed!")
except Exception as e:
    print("Error caught:", e)
num = int(input("Enter number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime Number")
else:
    print("Not Prime")

num = int(input("Enter number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)


text = input("Enter text: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
n = int(input("How many terms: "))
a, b = 0, 1

for i in range(n):
    print(a)
    a, b = b, a + b
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)

num = int(input("Enter number: "))
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** 3
    temp //= 10

if total == num:
    print("Armstrong Number")
else:
    print("Not Armstrong")

num = int(input("Enter number: "))
s = 0

while num > 0:
    digit = num % 10
    s += digit
    num //= 10

print("Sum =", s)


def reverse_string(text):
    return "".join(reversed(text))

print(reverse_string("Python"))

colors = ["Red", "Blue", "Green", "Yellow"]

print("Ascending:", sorted(colors))
print("Descending:", sorted(colors, reverse=True))   '''

















































