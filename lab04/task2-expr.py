import math

def func(a, b, c, x):
    d = 2
    e = 4
    f = 7

    print(f"Calculating the result of an expression √({a} ∙ cos {b} + exp({c}) + log(({d} ^ {x} + {e}), {f})")

    return math.sqrt(a * math.cos(b) + math.exp(c)) + math.log(d ** x + e), f)

def main():
    try:
        a = float(input('Input a: '))
        b = float(input('Input b: '))
        c = float(input('Input c: '))
        x = float(input('Input x: '))
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    # Calculate and print the result of the expression
    try:
        print(f"X = {func(a, b, c, x)}")
    except ValueError as e:
        print(f"Expression does not make sense at x = {x}")
        return

if __name__ == "__main__":
    main()