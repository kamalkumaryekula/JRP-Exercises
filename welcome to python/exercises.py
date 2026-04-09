# Personal Greeting: Ask the user for their name and print a personalized greeting like "Hello, [Name]! Welcome to Python programming."

name = input("please enter your name: ")
print(f'Hello, {name}! Welcome to python programming.')

# Rectangle Calculator: Input length and width of a rectangle. Calculate and display the area (length × width) and perimeter (2 × (length + width)).

l = int(input("Enter length of rectangle: "))
w = int(input("Enter width of rectangle: "))
area = l*w
perimeter = 2*(l+w)
print(f"area of rectangle is {area}, perimeter of reactangle is {perimeter}")

# Temperature Converter: Convert Celsius to Fahrenheit using the formula F = (C * 9/5) + 32. Display the result with proper formatting. 

c = int(input("Enter temperature in celsius: "))
f = (c*(9/5)) +32
print(f"Temperature in fahrenheit is {f}")

# Circle Properties: Given a radius, calculate diameter (2r), circumference (2πr), and area (πr²). Use math.pi for accuracy.

import math
r = int(input("Enter radius of the circle: "))
d = 2*r
c = 2*math.pi*r
a = 2*math.pi*r*r
print(f"Diameter of the circle is : {d}")
print(f"Circumference of the circle is: {c:.2f}")
print(f"Area of the circle is: {a:.2f}")

# Number Classifier: Determine if an integer is even or odd using the modulus operator (%). Print a clear message with the result.

i = int(input("Enter a number: "))
if i % 2 == 0:
    print("It is a even number.")
else:
    print("It is a odd number")

# Smart Tip Calculator: Calculate tip and total bill based on bill amount and tip percentage. Display a formatted receipt.

bill = int(input("Enter bill amount: "))
tip_per = int(input("Enter tip percentage: "))
total_bill = (bill * (tip_per/100)) + bill
print(f"The total bill is : {total_bill}")

# Age Calculator: Convert age in years to total days lived (assume 365.25 days/year for leap years).

age = int(input("Enter your age: "))
years_days = age * 365.25
print(f"your age in days are {years_days}")

# Variable Swapper: Demonstrate swapping two variables using Python's tuple unpacking: x, y = y, x.

x = int(input("Enter value of x : "))
y = int(input("Enter value of y : "))
x,y = y,x
print(f'values of x and y after swapping are {x},{y}')

# BMI Calculator: Calculate Body Mass Index from weight (kg) and height (m) using BMI = weight / (height ** 2). Provide health category interpretation.

weight = int(input("Enter your weight in kgs: "))
height = float(input("Enter your height in meters: "))
bmi = weight/(height**2)
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"
print(category)

# Time Formatter: Convert total seconds into hours:minutes:seconds format (e.g., 3661 → "1:01:01").

s= int(input("Enter time in seconds: "))
h = s//3600
m = s%3600//60
s_s = s%60
print(f"Time is {h}:{m}:{s_s}")

# Statistics Calculator: Input three numbers and compute their average, minimum, and maximum values.

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))
average = (a+b+c)/3
minimum = min(a,b,c)
maximum = max(a,b,c)
print(f"average of three numbers are {average:.2f}")
print(f"minimum of three are {minimum}")
print(f"maximum of three are {maximum}")

# Compound Interest: Calculate compound interest using the formula A = P(1 + r/n)^(nt) where P is principal, r is rate, n is compounds per year, t is time.

p = int(input("Enter principle amount: "))
r = int(input("Enter intrest rate: "))/100
n = int(input("Enter no of compounds per year: "))
t = int(input("Enter time period: "))
a = p*(1 + r/n)**(n*t)
print(f"compound intrest is {a:.2f}")