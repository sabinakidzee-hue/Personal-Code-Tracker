# Write a program to swap the first and last characters of the string “Python”.
str="Python"
print(str[-1]+str[1:-1]+str[0])
# Write a program to print the second last character of the string “Programming”.
str="Programming"
print(str[-2])
# Write a program to print the first three characters individually using indexing (not slicing) from “Elephant”.
str="Elephant"
print(str[0])
print(str[1])
print(str[2])
# Write a program to check if the first and last character are the same in the string "radar".
str="radar"
if str[0]==str[-1]:
    print("The first and last characters are the same.")
# Write a program to replace a character at a specific index (e.g., index 3 with "X") in "abcdef".
str="abcdef"
index=3
new_char="X"
new_str=str[:index]+new_char+str[index+1:]
print(new_str)
# Write a program to print characters at even indexes from "Development".
str="Development"
for i in range(0,len(str),2):
    print(str[i])
# Write a program to print characters at odd indexes from "Information".
str="Information"
for i in range(1,len(str),2):
    print(str[i])
# Write a program to create a new string using the first, middle, and last characters of "Programming".
str="Programming"
middle_index=len(str)//2
new_str=str[0]+str[middle_index]+str[-1]
print(new_str)

# Write a program to print the characters from last to first without slicing using negative indexing.
str="Hello"
for i in range(-1,-len(str)-1,-1):
    print(str[i])
# Write a program to access a substring using negative indexes (e.g., last 4 to last 2 characters).
str="HelloWorld"
substring=str[-4:-1]

# Write a program to check if the second and second-last characters are the same.
str="abccba"
if str[1]==str[-2]:
    print("The second and second-last characters are the same.")
# Write a program to extract the first 3 and last 3 characters of a string using slicing.
str="abcdefghij"
new_str=str[:3]+str[-3:]
print(new_str)
# Write a program to remove the first and last character from a string using slicing.
str="abcdefghij"
new_str=str[1:-1]
print(new_str)
# Write a program to get the middle part of a string (excluding the first 2 and last 2 characters).
str="abcdefghij"
new_str=str[2:-2]

# Given s = “12345”, write a program to check whether s contains only digits using .isdigit().
s = "12345"
if s.isdigit():
    print(f"{s} contains only digits.")

# Given s = “Python3”, write a program to check whether s contains only letters and numbers using .isalnum().
s = "Python3"
if s.isalnum():
    print(f"{s} contains only letters and numbers.")
# Given s = “hello”, write a program to check whether s is in lowercase using .islower().
s = "hello"
if s.islower():
    print(f"{s} is in lowercase.")

