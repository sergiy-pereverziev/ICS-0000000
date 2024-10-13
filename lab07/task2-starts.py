import re

def main():
    print("Let's count number of words starting with the same symbol(s)")
    try:
        num_symbols = int(input("Which prefix length to use? "))
        if (num_symbols < 1):
            raise ValueError("please input a positive integer")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    words = []

    while True:
        word = input("Input next word (empty to end): ")
        if not word:
            break

        words.append(word)

    prefix_occurrences = {}
    for word in words:
        key = word[:num_symbols]
        if not key in prefix_occurrences:
            prefix_occurrences[key] = 0

        prefix_occurrences[key] += 1

    repeats = {prefix: times for prefix, times in prefix_occurrences.items() if times > 1}
    total = sum(repeats.values())

    if not total:
        print(f"No repeats in prefixes of length {num_symbols}")
        return

    print(f"Total repeats: {total}")
    print("Repeats by prefix:")
    for prefix, times in sorted(repeats.items(), key = lambda item: item[1]):
        print(f"'{prefix}': {times} occurrences")

if __name__ == "__main__":
    main()