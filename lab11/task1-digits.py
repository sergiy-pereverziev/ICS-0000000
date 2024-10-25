import csv

def main():
    print("CSV report on the input number")
    while True:
        try:
            x = int(input('Input x: '))
            if not 100 <= x < 1000:
                raise ValueError('x should be a three digit number')
            break
        except ValueError as e:
            print(f"Invalid input: {e}")
            continue
    
    digits = sorted(list(str(x)))

    filename = 'digits.csv'
    with open(filename, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['min', 'max', 'med'])
        writer.writeheader()
        writer.writerow({ 'min': digits[0], 'max': digits[2], 'med': digits[1] })

if __name__ == "__main__":
    main()