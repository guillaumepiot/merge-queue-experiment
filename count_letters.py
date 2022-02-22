import sys
import string

def count_letters(input):
    letters = [char for char in input if char in string.ascii_letters]
    count = len(letters)

    if count == 0:
        print(f"Empty string!")
    elif count == 1:
        print(f"There is {count} letter in this string.")
    else:
        print(f"There are {count} letters in this string.")

if __name__ == "__main__":

    try:
        input = sys.argv[1]
        count_letters(input)
    except IndexError:
        print("No string submitted.")

    
