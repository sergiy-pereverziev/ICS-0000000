from func import func
from renderer import print_table

def main():
    print("Tabulating function from a to b with a step of h")
    try:
        a = int(input('Input a: '))
        b = int(input('Input b: '))
        h = int(input('Input h: '))
        value_range = range(a, b, h)
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    values: list[tuple[float, float]] = []

    for x in value_range:
        values.append([x, func(x)])

    print_table(values)

if __name__ == "__main__":
    main()