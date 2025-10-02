#Given sentence = “Coding is fun”, write a program to check how many words are alphabetic.
sentence = "Coding is fun"
words = sentence.split()
count = sum(1 for word in words if word.isalpha())
print(f"Number of alphabetic words: {count}")
#Given username = “User123”, write a program to check if it is alphanumeric and starts with a letter.
username = "User123"
if username.isalnum() and username[0].isalpha():
    print(f"{username} is alphanumeric and starts with a letter.")
else:
    print(f"{username} does not meet the criteria.")

#Write a Python program to demonstrate how a global variable can be updated inside a function. Define a global variable count = 0. Write a function increment() that increases count by 1 each time it is called. Use a while loop to call increment() repeatedly until count becomes 5 and print the value of count after each increment.
count = 0
def increment():
    global count
    count += 1
while count < 5:
    increment()
    print(f"Count after increment: {count}")
#Write a Python program to print the Fibonacci series up to n terms using a while loop. Ask the user for the number of terms n.
n = int(input("Enter the number of terms for Fibonacci series: "))  
a, b = 0, 1
count = 0
print("Fibonacci series:")
while count < n:
    print(a, end=' ')
    a, b = b, a + b
    count += 1
print()
#Write a Python program where a function uses a local variable to check whether a number entered by the user is even or odd. The function check_number() should take a number from the user, store its status (even or odd) in a local variable, and print “Even number!” or “Odd number!”. Ask the user repeatedly using a while loop to enter numbers until they type -1 to stop.
def check_number():
    num = int(input("Enter a number (-1 to stop): "))
    if num == -1:
        return False
    status = "Even number!" if num % 2 == 0 else "Odd number!"
    print(status)
    return True
while True:
    if not check_number():
        break


#Write a Python program that uses a global variable to keep track of how many items the user 
# has added to a shopping cart. Define a global variable cart_count = 0. Write a function add_to_cart() that increases cart_count by 1 each time it is called. Use a while loop to repeatedly ask the user if they want to add an item to the cart (y/n). If the user enters 'y', call add_to_cart() and print the current cart_count. If the user enters 'n', exit the loop and print the final cart_count.
cart_count = 0
def add_to_cart():
    global cart_count
    cart_count += 1
while True:
    choice = input("Do you want to add an item to the cart? (y/n): ").lower()
    if choice == 'y':
        add_to_cart()
        print(f"Current cart count: {cart_count}")
    elif choice == 'n':
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
print(f"Final cart count: {cart_count}")



