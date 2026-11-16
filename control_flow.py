numbers = [10, -5, 0, 8, -3, 7, 0]

for num in numbers:
    if num > 0:
        print(f"{num} is Positive")
    elif num < 0:
        print(f"{num} is Negative")
    else: 
        print(f"{num} is Zero")

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

for num in range(6):
    print(f"Factorial of {num} is {factorial(num)}")

number = 17 

if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")

total_sum = 0 

for i in range(1, 11):
    total_sum += i
print(f"Sum of first 10 natural numbers is {total_sum}")

score = 85 

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")
print(f"Grade for score {score} is: {grade}")

def fibonacci(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

print(f"Fibonacci sequence up to 10 terms: {fibonacci(10)}")