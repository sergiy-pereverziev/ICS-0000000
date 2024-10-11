import sys

def sum_of_digits(number):
    # Split the number into its digits and return the sum
    return sum(int(digit) for digit in str(number))

def validate_two_digit_number(number, label):
    # Check if the input is a two-digit number
    if not (number.isdigit() and 10 <= int(number) <= 99):
        raise ValueError(f'{label} must be a two-digit number.')

def main():
    # Check if exactly two arguments are passed (excluding the script name)
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <first_number> <second_number>")
        return

    try:
        # Get the numbers from the command-line arguments
        first_number = sys.argv[1]
        second_number = sys.argv[2]

        # Validate the inputs
        validate_two_digit_number(first_number, "first parameter")
        validate_two_digit_number(second_number, "second parameter")

        # Convert the valid inputs to integers
        first_number = int(first_number)
        second_number = int(second_number)
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    # Calculate and print the sum of the digits
    total_sum = sum_of_digits(first_number) + sum_of_digits(second_number)
    print(f"The sum of the digits is: {total_sum}")

if __name__ == "__main__":
    main()