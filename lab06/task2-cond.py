from func import func
from renderer import print_table

def main():
    print("Tabulating function from a to b with a step of h")
    try:
        a = float(input('Input a: '))
        b = float(input('Input b: '))
        h = float(input('Input h: '))
        if (h == 0):
            raise ValueError("Step cannot be zero")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    values: list[tuple[float, float]] = []

    x = a
    while (h < 0 and x > b) or (h > 0 and x < b):
        values.append([x, func(x)])
        x += h

    print_table(values)

if __name__ == "__main__":
    main()