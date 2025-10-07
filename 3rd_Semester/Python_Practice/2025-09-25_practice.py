
#Write a Python program to swap two numbers without using a third variable.
a=5
b=10
a,b=b,a
print("a=",a)
print("b=",b)
# Write a Python program that accepts two numbers and an operator (+, −, *, /) from the user and performs the operation.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter an operator (+, -, *, /): ")
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator!"
print(f"The result is: {result}")
# Write a Python program to find the largest of three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print(f"The largest number is: {largest}")

# Write a Python program to accept marks of five subjects from the user, calculate total and average marks, and display the grade (A/B/C/Fail).
marks = []
for i in range(5):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)
total = sum(marks)
average = total / 5
if average >= 90:
    grade = 'A'
elif average >= 75:
    grade = 'B'
elif average >= 50:
    grade = 'C'
else:
    grade = 'Fail'
print(f"Total Marks: {total}, Average Marks: {average}, Grade: {grade}")

# Write a Python program to calculate the sum of first n natural numbers using a while loop.'
n = int(input("Enter a positive integer: "))
sum_n = 0
i = 1
while i <= n:
    sum_n += i
    i += 1
print(f"The sum of the first {n} natural numbers is: {sum_n}")

# Write a Python program to reverse the digits of a number using a while loop.
num = int(input("Enter a number: "))
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print(f"The reversed number is: {reversed_num}")

# Write a Python program to count the number of digits in an integer using a while loop.
num = int(input("Enter a number: "))
count = 0
temp = abs(num)  # Handle negative numbers
while temp > 0:
    count += 1
    temp //= 10
print(f"The number of digits in {num} is: {count}")

# Write a Python program that repeatedly asks the user for a password until the correct password “python123” is entered.
correct_password = "python123"
while True:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Access granted.")
        break
    else:
        print("Incorrect password. Try again.")

# Write a Python program to print numbers from 1 to n except multiples of 3 using a while loop and continue statement
n = int(input("Enter a positive integer: "))
i = 1
while i <= n:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1

# Write a Python program to repeatedly accept numbers from the user. Stop when the user enters a negative number. Finally, print the sum of all positive numbers entered.
total_sum = 0
while True:
    num = float(input("Enter a number (negative to stop): "))
    if num < 0:
        break
    total_sum += num
print(f"The sum of all positive numbers entered is: {total_sum}")

#Write a Python function factorial() that takes a positive integer and returns its factorial. Ask the user for a number, call the function, and print the factorial.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a positive integer: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is: {result}")
# Write a Python function to check if a number is prime. Ask the user for a number, call the function, and print whether the number is prime or not.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a positive integer: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
    

