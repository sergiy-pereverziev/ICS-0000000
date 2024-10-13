import math

def func(x):
    xa = -1.2
    xb = 0.53
    a1 = 3
    b1 = 0.127
    c1 = 2
    a2 = 2.35
    b2 = 4
    c2 = 1
    a3 = 0.11
    b3 = 3

    print(f"Calculating the function 𝑓(𝑥) = ({a1} - {b1}𝑥 + ln |𝑥 + 2|, 𝑥 > {xb})  &  ({a2} ∙ exp({b2}𝑥 - {c2}) + cos 𝑥, {xa} < x <= {xb})  &  ({a3}√(𝑥 + {b3} cos 𝑥), x <= {xa}).")

    if (x > xb):
        return a1 - b1*x + math.log(math.fabs(x + 2))
    elif (x <= xa):
        # It's a little weird that the function is never defined for x <= -1.2 but it's a part of the task so anyway
        return a3 * math.sqrt(x + b3 * math.cos(x))
    else:
        return a2 * math.exp(b2 * x - c2) + math.cos(x)

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