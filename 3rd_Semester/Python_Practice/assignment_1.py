# Define a Python function named generate bill(item, price, quantity=1,
# discount=0, tax rate=0.05) that calculates and prints the final payable amount
# for a purchased item after applying the discount and adding tax. The function should
# use default arguments for quantity, discount, and tax rate.
# The function should perform the following steps:
# • Compute the subtotal = price × quantity.
# • Apply a discount percentage on the subtotal.
# • Apply a tax (default = 5%) on the discounted amount.
# • Print a detailed bill summary showing item name, quantity, price, discount, tax,
# and total amount.
# Call the function in different ways:
# i. Using only the required arguments (item and price).
# ii. Providing a custom quantity while keeping default discount and tax.
# iii. Using named arguments for discount and tax while keeping default quantity.
# iv. Providing all arguments explicitly.
# Example:
# Item: Laptop, Quantity: 2, Price: 50000, Discount: 10%, Tax: 5%
# Total Bill: 94500.0

# L2, L3
def generate_bill(item, price, quantity=1, discount=0, tax_rate=0.05):
    subtotal = price * quantity
    discount_amount = subtotal * (discount / 100)
    discounted_total = subtotal - discount_amount
    tax_amount = discounted_total * tax_rate
    total_amount = discounted_total + tax_amount

    print("----- Bill Summary -----")
    print(f"Item: {item}")
    print(f"Quantity: {quantity}")
    print(f"Price per item: {price}")
    print(f"Subtotal: {subtotal}")
    print(f"Discount: {discount}% (-{discount_amount})")
    print(f"Tax: {tax_rate * 100}% (+{tax_amount})")
    print(f"Total Amount Payable: {total_amount}")
    print("------------------------")


# Q2. Design and implement a Python program that simulates a simple calculator using
# if-elif statements.
# The program should allow the user to choose an operation :— addition, subtraction,
# multiplication, division, or modulus and then input two numbers.
# The program should perform the selected arithmetic operation based on the user’s
# choice and display the result in a clear and readable format.
# It should also handle division and modulus by zero using conditional checks and
# display an appropriate warning message.
# Input: Operation choice (add, sub, mul, div, mod) and two numbers entered by the
# user.
# Output: Display the result of the chosen operation or show a warning message if
# division or modulus by zero is attempted.
# Example: Enter operation (add/sub/mul/div/mod): div
# Enter first number: 10
# Enter second number: 0
# Error: Division by zero not allowed.
operation = input("Enter operation (add/sub/mul/div/mod): ").strip().lower()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = None
if operation == "add":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif operation == "sub":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif operation == "mul":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif operation == "div":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Division by zero not allowed.")
elif operation == "mod":
    if num2 != 0:
        result = num1 % num2
        print(f"Result: {num1} % {num2} = {result}")
    else:
        print("Error: Modulus by zero not allowed.")
else:
    print("Error: Invalid operation selected.")

# Q3. Design and implement a Python program that accepts the name of a month from the
# user as a string input. The program should determine and display the number of days
# in the specified month. For February, the program should identify the year (leap or
# non-leap year) first, before determining the number of days (28 or 29 days).
# Make use of Dictionary data structures for mapping months to their corresponding
# number of days. Handle both valid and invalid inputs by displaying an error message
# if the entered month name is incorrect.
# Input:
# Enter the name of a month: February
# Enter a year: 2024
# Output:
# February 2024 has 29 days.
month_days = {
    "january": 31,
    "february": 28,  # Default, will adjust for leap years
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "august": 31,
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31
}
month = input("Enter the name of a month: ").strip().lower()
if month in month_days:
    if month == "february":
        year = int(input("Enter a year: "))
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days = 29
        else:
            days = 28
        print(f"{month.capitalize()} {year} has {days} days.")
    else:
        days = month_days[month]
        print(f"{month.capitalize()} has {days} days.")
else:
    print("Error: Invalid month name entered.")

# Q4. Design and implement a Python program for two approaches for checking whether
# a given string is a palindrome using two separate functions.
# The first function should use a for loop to determine whether the given string is
# a palindrome. It should ignore only case differences (for example, “Madam” and
# “madam” should be treated as the same).
# The second function should use the two-pointer technique to check whether a
# string is a palindrome. This function should ignore case, spaces, and punctuation
# so that complete sentences such as “A man, a plan, a canal: Panama” can be correctly
# identified as palindromes.
# Finally, call both functions in the main program using the user input and display the
# results from both approaches for comparison.
# Input: A string entered by the user (e.g., “Madam”)
# Output: Display the results from both palindrome-checking functions. For example:
# For-loop Check: Palindrome, Two-pointer Check: Palindrome
def is_palindrome_for_loop(s):
    s = s.lower()
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True
def is_palindrome_two_pointer(s):
    import string
    s = ''.join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
user_input = input("Enter a string to check for palindrome: ")
result_for_loop = is_palindrome_for_loop(user_input)
result_two_pointer = is_palindrome_two_pointer(user_input)
print(f"For-loop Check: {'Palindrome' if result_for_loop else 'Not a Palindrome'}")
print(f"Two-pointer Check: {'Palindrome' if result_two_pointer else 'Not a Palindrome'}")

# Q5. Design and implement a Python program that reads a decimal number from the user
# and performs multiple base conversions. The program should:

# • Convert the decimal number into its Binary, Octal, and Hexadecimal repre-
# sentations using the built-in functions.

# • Display all three converted values without their prefixes (0b, 0o, 0x).
# • Count and display the number of digits in each converted representation.
# • Reverse the conversion — convert the binary, octal, and hexadecimal strings

# back to decimal using the int(string, base) function — and display the re-
# sults to verify correctness.

# Input: A decimal number entered by the user (e.g., 255).
# Output: Display the binary, octal, and hexadecimal forms (without prefixes) and

# their digit counts. Then show the decimal values obtained by reconverting each rep-
# resentation.

decimal_number = int(input("Enter a decimal number: "))
binary_rep = bin(decimal_number)[2:]
octal_rep = oct(decimal_number)[2:]
hex_rep = hex(decimal_number)[2:].upper()
print(f"Binary: {binary_rep} (Digits: {len(binary_rep)})")
print(f"Octal: {octal_rep} (Digits: {len(octal_rep)})")
print(f"Hexadecimal: {hex_rep} (Digits: {len(hex_rep)})")


# Q6. Design and implement a Python program that performs both encryption and decryp-
# tion of a string.
# The encryption function should first reverse the input string and then swap every
# adjacent pair of characters to generate the encrypted text. The decryption function
# should reverse this process to obtain the original string.
# Input: A string entered by the user (e.g., “hello”)
# Output: Display both the encrypted and decrypted strings.
# For example: Encrypted: eholl, Decrypted: hello
def encrypt(text):
    reversed_text = text[::-1]
    encrypted_chars = list(reversed_text)
    for i in range(0, len(encrypted_chars) - 1, 2):
        encrypted_chars[i], encrypted_chars[i + 1] = encrypted_chars[i + 1], encrypted_chars[i]
    return ''.join(encrypted_chars)
def decrypt(encrypted_text):
    decrypted_chars = list(encrypted_text)
    for i in range(0, len(decrypted_chars) - 1, 2):
        decrypted_chars[i], decrypted_chars[i + 1] = decrypted_chars[i + 1], decrypted_chars[i]
    return ''.join(decrypted_chars)[::-1]
user_string = input("Enter a string to encrypt: ")
encrypted_string = encrypt(user_string)
decrypted_string = decrypt(encrypted_string)
print(f"Encrypted: {encrypted_string}")
print(f"Decrypted: {decrypted_string}")


# Q7. Develop a Python program that reads a sentence from the user, splits it into words,
# sorts them in reverse alphabetical order, and joins them using a custom separator
# provided by the user.
# The program should ignore punctuation marks during processing so that only valid
# words are considered for sorting.
# Input: A sentence and a custom separator entered by the user (e.g., “Hello, world!
# Python.”, “—”).
# Output: Display the sorted words joined by the specified separator.
# For example: world—python—hello

import string
sentence = input("Enter a sentence: ")
separator = input("Enter a custom separator: ")
words = [''.join(c for c in word if c.isalnum()) for word in sentence.split()]
words = [word for word in words if word]  # Remove empty strings
sorted_words = sorted(words, key=str.lower, reverse=True)
result = separator.join(sorted_words)
print(f"Sorted and joined words: {result}")

# Q8. Design and implement a Python function named validate password(password)
# that checks whether a given password meets specific security requirements. The
# function should validate the password based on the following rules:
# • The password must contain at least 8 characters.
# • It must include at least one uppercase letter (A–Z).
# • It must include at least one lowercase letter (a–z).
# • It must include at least one digit (0–9).

# • It must include at least one special character from the set !@#$% and no white-
# spaces.

# The function should return:
# • True if the password satisfies all the above conditions.

# • False, along with a list of specific error messages, if one or more rules are vio-
# lated.

# Input: A string representing the password entered by the user (e.g., “Pass@123”).

# Output: Display whether the password is valid or invalid, and if invalid, list the vio-
# lated rules.

def validate_password(password):
    errors = []
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    if not any(c.isupper() for c in password):
        errors.append("Password must include at least one uppercase letter (A-Z).")
    if not any(c.islower() for c in password):
        errors.append("Password must include at least one lowercase letter (a-z).")
    if not any(c.isdigit() for c in password):
        errors.append("Password must include at least one digit (0-9).")
    if not any(c in "!@#$%" for c in password):
        errors.append("Password must include at least one special character (!@#$%).")
    if any(c.isspace() for c in password):
        errors.append("Password must not contain any white spaces.")
    
    if errors:
        return False, errors
    return True, []
user_password = input("Enter a password to validate: ")
is_valid, error_messages = validate_password(user_password)
if is_valid:
    print("Password is valid.")
else:
    print("Password is invalid. Issues:")
    for msg in error_messages:
        print(f"- {msg}")

# Q9. Develop a Python program that processes a paragraph of text entered by the user.
# The program should perform the following tasks:
# • Convert the entire paragraph into title case (each word starts with a capital
# letter).
# • Remove extra spaces between words using the split() and join() methods.

# • Count and display the occurrences of each vowel (A, E, I, O, U) using their char-
# acter codes.

# Input: A paragraph entered by the user (e.g., “ this is an example paragraph ”).
# Output: Display the cleaned and title-cased paragraph, followed by the count of each
# vowel.
# For example: Processed Text: This Is An Example Paragraph
# Vowel Counts  A: 3, E: 2, I: 1, O: 0, U: 0

user_paragraph = input("Enter a paragraph: ")
title_cased = ' '.join(user_paragraph.split()).title()
print(f"Processed Text: {title_cased}")
vowel_counts = {vowel: 0 for vowel in "AEIOU"}
for char in title_cased.upper():
    if char in vowel_counts:
        vowel_counts[char] += 1
print("Vowel Counts:", ', '.join(f"{vowel}: {count}" for vowel, count in vowel_counts.items()))


# Q10. Develop a Python program that counts the frequency of each word in a given sen-
# tence while ignoring case and punctuation.

# The program should process the sentence, remove punctuation marks, convert all
# words to lowercase, and then count how many times each unique word appears.
# Finally, display the word frequencies in a formatted string sorted alphabetically by
# word.
# Input: A sentence entered by the user (e.g., “Hello world, hello!”).
# Output: Display the sorted word frequencies in the format “word: count“.
# For example: hello: 2 world: 1
import string
sentence = input("Enter a sentence: ")
words = [''.join(c for c in word if c.isalnum()).lower() for word in sentence.split()]
words = [word for word in words if word]  # Remove empty strings
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1
for word in sorted(word_freq):
    print(f"{word}: {word_freq[word]}")
    