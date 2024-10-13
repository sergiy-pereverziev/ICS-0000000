import sys, math

def func(x):
    a = 3
    b = 3.19
    c = 4
    d = 1
    e = 0.7

    print(f"Calculating the function 𝑓(𝑥) = {a}ᐨˣ ∙ √|{b}𝑥| + log(|𝑥 + {d}|, {c}) / (|𝑥 + {d}| + {e})")

    abs_x_plus_d = math.fabs(x + d)
    return math.pow(a, -x) * math.sqrt(math.fabs(b * x)) + math.log(abs_x_plus_d, c) / (abs_x_plus_d + e)

def main():
    try:
        x = float(input('Input x: '))
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    # Calculate and print the value of the function
    try:
        print(f"f(x) = {func(x)}")
    except ValueError as e:
        print(f"Function is not defined at x = {x}")
        return

if __name__ == "__main__":
    main()