import random, time

def generate(length: int):
    colors = "🟥🟧🟨🟩🟦🟪⬜"
    result = []
    for i in range(length):
        index = random.randint(0, len(colors) - 1)
        result.append(colors[index])
    return result

def check_result(items: list[str]):
    if (len(items) <= 1):
        raise ValueError("Must be at least 2 elements in a row")

    for i in range(1, len(items)):
        if items[0] != items[i]:
            return False
        
    return True

def main():
    print("Welcome to one-armed bandit simulator")
    slots = 3
    num_consecutive_runs = 1

    while True:
        move = input("Hit enter to play or enter q to exit: ")
        if move == "q":
            return
        elif move == "":
            print("The wheels are spinning...")
            time.sleep(0.5)
            combination = generate(slots)
            print(f"Result: {combination}")
            if (check_result(combination)):
                print(f"⭐⭐⭐ Wohoo! You won! Congrats!!! Took you {num_consecutive_runs} tries!⭐⭐⭐\n")
                num_consecutive_runs = 1
            else:
                print("Maybe next time...")
                num_consecutive_runs += 1
        else:
            print(f"Unknown command: {move}")


if __name__ == "__main__":
    main()