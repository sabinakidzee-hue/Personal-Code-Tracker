# def count(s, c) :
#     res = 0
    
#     for i in range(len(s)) :
#         if (s[i] == c):
#             res = res + 1
#     return res

# str= input("Enter a string: ")
# c = input("Enter the character to count: ")
# print(count(str, c))

# def remove_vowels(input_string):

#   vowels = "aeiouAEIOU"
#   new_string = ""
#   for char in input_string:
#     if char not in vowels:
#       new_string += char
#   return new_string

# user_input = input("Enter a string: ")
# result_string = remove_vowels(user_input)
# print("The string after removing vowels is: ",result_string)


# str=input("Enter a string: ")
# str[0]="s"
# print(str)

# str=input("Enter a string: ")
# str_upper=str[0].upper()
# rest_str=str[1:]
# print(str_upper+rest_str)

# def remove_duplicate(s):
#     new_str = ""
#     prev_char = ""
#     for char in s:
#         if char != prev_char:
#             new_str += char
#         prev_char = char
#     return new_str

def count_case(s):
    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return upper, lower

user_input = input("Enter a string: ")
upper_count, lower_count = count_case(user_input)
print(f"Uppercase letters: {upper_count}, Lowercase letters: {lower_count}")