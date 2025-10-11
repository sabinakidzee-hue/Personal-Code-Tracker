# Write a program to find the first occurrence of a substring "is" in "This is Python".
first_index = "This is Python".find("is")
print(f"First occurrence of 'is': {first_index}")

# Write a program to find the last occurrence of "a" in "Banana".
last_index = "Banana".rfind("a")
print(f"Last occurrence of 'a': {last_index}")

# Write a program to count how many times "the" appears in "the weather is the best".
count_the = "the weather is the best".count("the")
print(f"'the' appears {count_the} times")
print(f"'the' appears {count_the} times")

# Write a program to replace all occurrences of "cat" with "dog" in a sentence.
sentence = "The cat sat on the mat with another cat."
new_sentence = sentence.replace("cat", "dog")
print(f"After replacement: {new_sentence}")

# Write a program to check if a substring "Python" exists in "I love Python programming" and print its position.
sentence = "I love Python programming"
position = sentence.find("Python")
if position != -1:
    print(f"'Python' found at position: {position}")
else:
    print("'Python' not found")

# Write a program that takes a word from the user and replaces it with "***" in a given sentence.
user_word = input("Enter a word to replace: ")
given_sentence = "This is a sample sentence for testing."
modified_sentence = given_sentence.replace(user_word, "***")
print(f"Modified sentence: {modified_sentence}")

# Write a program to replace only the first occurrence of "apple" with "orange" in a sentence.
sentence = "apple banana apple grape apple"
new_sentence = sentence.replace("apple", "orange", 1)
print(f"After replacing first occurrence: {new_sentence}")

# Write a program to remove leading and trailing spaces from the string “ Hello World “.
trimmed_string = " Hello World ".strip()
print(f"Trimmed string: '{trimmed_string}'")

# Write a program to remove only leading spaces from “ Python”.
leading_trimmed = " Python".lstrip()
print(f"Leading spaces removed: '{leading_trimmed}'")

# Write a program to remove only trailing spaces from “Python “.
trailing_trimmed = "Python ".rstrip()
print(f"Trailing spaces removed: '{trailing_trimmed}'")

# Write a program to remove a specific character (e.g., *) from both ends of the string “***Hello***”.
cleaned_string = "***Hello***".strip("*")
print(f"Cleaned string: '{cleaned_string}'")

# Write a program to clean a user’s input (remove spaces before and after) before printing it.
user_input = input("Enter something with extra spaces: ").strip()
print(f"Cleaned input: '{user_input}'")

# Write a program to split the string “Python is fun” into a list of words.
words_list = "Python is fun".split()
print(f"List of words: {words_list}")

# Write a program that takes a sentence and splits it into words, then prints each word on a new line.
sentence = input("Enter a sentence: ")
words = sentence.split()
for word in words:
    print(word)
    
# Write a program to split a string based on “:” and join the resulting list with “|”.
split_string = "key1:value1:key2:value2"
parts = split_string.split(":")
joined_string = "|".join(parts)
print(f"Joined string: {joined_string}")

# Take a sentence from the user, convert it to title case, replace “Python” with “Java”, and print the result.
user_sentence = input("Enter a sentence: ")
modified_sentence = user_sentence.title().replace("Python", "Java")
print(f"Modified sentence: {modified_sentence}")

# Remove extra spaces from a string, then split it into words and join them back with “-“
messy_string = "  This   is  a   messy   string  "
cleaned = ' '.join(messy_string.split())
joined_with_hyphen = '-'.join(cleaned.split())
print(f"Joined with hyphen: {joined_with_hyphen}")

# Write a program that takes a sentence and counts how many words start with an uppercase letter.
sentence = input("Enter a sentence: ")
words = sentence.split()
count_uppercase = sum(1 for word in words if word.istitle())
print(f"Number of words starting with uppercase letter: {count_uppercase}")

# Given “ python is GREAT “, write a program to:
# Remove spaces
# Convert to lowercase
# Replace “great” with “awesome”
original_string = " python is GREAT "
cleaned_string = original_string.strip().lower().replace("great", "awesome")
print(f"Final string: '{cleaned_string}'")

