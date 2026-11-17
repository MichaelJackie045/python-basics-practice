import os 
import datetime
import math

cwd = os.getcwd()
print(f"Currwent working directory: {cwd}")

now = datetime.datetime.now()
print(f"Current date and time: {now}")

num = 5
factorial = math.factorial(num)
print(f"The factorial of {num} is {factorial}")