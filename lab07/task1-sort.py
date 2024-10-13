import re

def main():
    print("Listing words longer to shorter")
    lines = []
    for i in range(0, 2):
        lines.append(input(f"Input line {i + 1}: "))

    trimmer = lambda line: line.strip()
    single_line = " ".join(map(trimmer, lines))
    single_list = re.split(r"\s+", single_line)
    unique_list = list(set(single_list))

    print(sorted(unique_list, key = len, reverse = True))

if __name__ == "__main__":
    main()