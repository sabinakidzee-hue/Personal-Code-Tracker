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
def bill(itm, pr, qty=1, disc=0, tax=0.05):
    sub = pr * qty
    dis_amt = sub * (disc / 100)
    dis_total = sub - dis_amt
    tax_amt = dis_total * tax
    total = dis_total + tax_amt

    print("---- BILL ----")
    print(f"Item: {itm}")
    print(f"Qty: {qty}, Price: {pr}")
    print(f"Disc: {disc}% (-{dis_amt})")
    print(f"Tax: {tax*100}% (+{tax_amt})")
    print(f"Total: {total}")
    print("--------------")


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
# Q2
op = input("Op (add/sub/mul/div/mod): ").lower()
a = float(input("1st num: "))
b = float(input("2nd num: "))

if op == "add":
    print(a + b)
elif op == "sub":
    print(a - b)
elif op == "mul":
    print(a * b)
elif op == "div":
    print("Err: /0" if b == 0 else a / b)
elif op == "mod":
    print("Err: %0" if b == 0 else a % b)
else:
    print("Invalid op")


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
# Q3
mon_days = {
    "jan": 31, "feb": 28, "mar": 31, "apr": 30,
    "may": 31, "jun": 30, "jul": 31, "aug": 31,
    "sep": 30, "oct": 31, "nov": 30, "dec": 31
}
m = input("Month: ").strip().lower()
if m in mon_days:
    if m == "feb":
        y = int(input("Year: "))
        d = 29 if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) else 28
        print(f"Feb {y} has {d} days")
    else:
        print(f"{m.title()} has {mon_days[m]} days")
else:
    print("Wrong month!")

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
# Q4
def pali1(s):
    s = s.lower()
    for i in range(len(s)//2):
        if s[i] != s[-(i+1)]:
            return False
    return True

def pali2(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    l, r = 0, len(s)-1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

txt = input("Enter: ")
print("Loop:", "Yes" if pali1(txt) else "No")
print("2Ptr:", "Yes" if pali2(txt) else "No")


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

# Q5
n = int(input("Dec num: "))
b = bin(n)[2:]
o = oct(n)[2:]
h = hex(n)[2:].upper()
print("Bin:", b, len(b))
print("Oct:", o, len(o))
print("Hex:", h, len(h))



# Q6. Design and implement a Python program that performs both encryption and decryp-
# tion of a string.
# The encryption function should first reverse the input string and then swap every
# adjacent pair of characters to generate the encrypted text. The decryption function
# should reverse this process to obtain the original string.
# Input: A string entered by the user (e.g., “hello”)
# Output: Display both the encrypted and decrypted strings.
# For example: Encrypted: eholl, Decrypted: hello
# Q6
def enc(t):
    t = t[::-1]
    t = list(t)
    for i in range(0, len(t)-1, 2):
        t[i], t[i+1] = t[i+1], t[i]
    return ''.join(t)

def dec(t):
    t = list(t)
    for i in range(0, len(t)-1, 2):
        t[i], t[i+1] = t[i+1], t[i]
    return ''.join(t)[::-1]

s = input("Text: ")
e = enc(s)
d = dec(e)
print("Enc:", e)
print("Dec:", d)



# Q7. Develop a Python program that reads a sentence from the user, splits it into words,
# sorts them in reverse alphabetical order, and joins them using a custom separator
# provided by the user.
# The program should ignore punctuation marks during processing so that only valid
# words are considered for sorting.
# Input: A sentence and a custom separator entered by the user (e.g., “Hello, world!
# Python.”, “—”).
# Output: Display the sorted words joined by the specified separator.
# For example: world—python—hello

# Q7
import string
s = input("Sentence: ")
sep = input("Separator: ")
w = [''.join(c for c in x if c.isalnum()) for x in s.split()]
w = [x for x in w if x]
w.sort(key=str.lower, reverse=True)
print(sep.join(w))


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

# Q8
def chk_pwd(p):
    err = []
    if len(p) < 8: err.append("min 8 chars")
    if not any(c.isupper() for c in p): err.append("1 uppercase")
    if not any(c.islower() for c in p): err.append("1 lowercase")
    if not any(c.isdigit() for c in p): err.append("1 digit")
    if not any(c in "!@#$%" for c in p): err.append("1 special")
    if any(c.isspace() for c in p): err.append("no space")
    return err

pw = input("Pwd: ")
e = chk_pwd(pw)
print("Valid" if not e else "Invalid:", ', '.join(e))


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

# Q9
p = input("Para: ")
t = ' '.join(p.split()).title()
print("Text:", t)
v = {x: 0 for x in "AEIOU"}
for c in t.upper():
    if c in v: v[c] += 1
print("Vowels:", v)

# Q10. Develop a Python program that counts the frequency of each word in a given sen-
# tence while ignoring case and punctuation.

# The program should process the sentence, remove punctuation marks, convert all
# words to lowercase, and then count how many times each unique word appears.
# Finally, display the word frequencies in a formatted string sorted alphabetically by
# word.
# Input: A sentence entered by the user (e.g., “Hello world, hello!”).
# Output: Display the sorted word frequencies in the format “word: count“.
# For example: hello: 2 world: 1
# Q10
import string
s = input("Sentence: ")
w = [''.join(c for c in x if c.isalnum()).lower() for x in s.split()]
w = [x for x in w if x]
f = {}
for x in w:
    f[x] = f.get(x, 0) + 1
for k in sorted(f):
    print(f"{k}: {f[k]}")
