import sys
import string

def count_letters_fn(input):
    letters = [char for char in input if char in string.ascii_letters]
    count = len(letters)

    if count == 0:
        return f"Empty string!"
    elif count == 1:
        return f"There is {count} letter in this string."
    else:
        return f"There are {count} letters in this string."

if __name__ == "__main__":
    
    try:
        input = sys.argv[1]
        print(count_letters_fn(input))
    except IndexError:
        print("No string submitted.")

    
