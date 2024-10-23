import numpy as np
import random

def main():
    print("Manipulating dictionary")

    try:
        numbers_line = input("Input integers 1 to 9 separated by spaces: ")
        translations_line = input("Input translations for the numbers: ")

        numbers = list(map(int, numbers_line.split(" ")))
        translations = translations_line.split(" ")

        for number in numbers:
            if number < 1 or number > 9:
                raise ValueError("Only numbers 1 to 9 are allowed")

        if len(numbers) != len(translations):
            raise ValueError("Number count and translations count mismatch")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return
    
    dictionary = dict(zip(numbers, translations))
    print(f"Dictionary formed: {dictionary}")

    inputs = 0

    while inputs < 5:
        try:
            number = int(input("Input another integer from 1 to 9: "))

            if number < 1 or number > 9:
                raise ValueError("Only numbers 1 to 9 are allowed")
            
            if number in dictionary:
                raise ValueError("This key is already in the dictionary")

            translation = input("Input its translation: ")
            
            dictionary[number] = translation
            inputs += 1
        except ValueError as e:
            print(f"Invalid input: {e}")
            continue
    
    print(f"Dictionary amended: {dictionary}")

    
if __name__ == "__main__":
    main()