# Write a program to assign a value 20 to a variable x and print it.
x = 20
print(x)
# Take a number x = 10, add 5 using +=, and print the result.
x = 10
x += 5
print(x)

# Start with y = 25, subtract 7 using -=, and display the final value.
y = 25
y -= 7
print(y)

# Assign 8 to a, then multiply it by 4 using *=, and print the result.
a = 8
a *= 4
print(a)    

# Take b = 100, divide it by 5 using /=, and show the output.
b = 100
b /= 5
print(b)

# Combine multiple assignment operators in one program:


# Start with x = 10
# Add 5
# Multiply by 3
# Subtract 7
# Divide by 2
# Print the final result.
x = 10
x += 5
x *= 3
x -= 7
x /= 2
print(x)

# Create a program where a user enters a number, and you repeatedly apply +=, -=, and *= operators to show how the value changes.
num = int(input("Enter a number: "))
num += 10
print(f"After adding 10: {num}")
num -= 5
print(f"After subtracting 5: {num}")
num *= 2
print(f"After multiplying by 2: {num}")

# Questions on if
# Write a program to check whether a number is even or odd.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Take a number from the user and check whether it is positive, negative, or zero.
num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# Write a program to check whether a person is eligible to vote (age ≥ 18).
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# Check if a number is divisible by 5 and 11.
num = int(input("Enter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print(f"{num} is divisible by both 5 and 11")
else:
    print(f"{num} is not divisible by both 5 and 11")

# Write a program to find the largest of two numbers using if.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 > num2:
    print(f"{num1} is larger")
else:
    print(f"{num2} is larger")
    
# Questions on while loop
# Print numbers from 1 to 10 using a while loop.
i = 1
while i <= 10:
    print(i)
    i += 1

# Write a program to print the multiplication table of a given number using while.
num = int(input("Enter a number for multiplication table: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

# Find the sum of digits of a number using a while loop.
num = int(input("Enter a number to find the sum of its digits: "))
sum_of_digits = 0
while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num //= 10
print(f"Sum of digits: {sum_of_digits}")

# Reverse a number using a while loop (e.g., 123 → 321).
num = int(input("Enter a number to reverse: "))
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print(f"Reversed number: {reversed_num}")

# Print all even numbers between 1 and 20 using while.
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

# Questions on for loop
# Print numbers from 1 to 100 using a for loop.
for i in range(1, 101):
    print(i)

# Write a program to print the square of numbers from 1 to 10.
for i in range(1, 11):
    print(f"Square of {i} is {i**2}")

# Print the elements of a list using a for loop.
my_list = [10, 20, 30, 40, 50]
for element in my_list:
    print(element)

# Write a program to print the factorial of a number using a for loop.
num = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is {factorial}")

