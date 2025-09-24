def longest_word():
    words = input("Enter a list of words separated by spaces: ").split()
    if not words:
        print("No words entered.")
        return
    longest = max(words, key=len)
    print(f"The longest word is: {longest}")

def remove_duplicate_words():
    words = input("Enter a list of words separated by spaces: ").split()
