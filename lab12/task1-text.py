import sys

def get_word_range(contents, start, end):
    clean_words = list(map(lambda word: word.strip(",."), filter(lambda word: word, " ".join(contents.split("\n")).split(" "))))

    if not start:
        return clean_words[:end]
    elif not end:
        return clean_words[start:]
    else:
        return clean_words[start:end]


def main():
    print("Analyzing the text file")

    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <file_name>")
        return

    try:
        file_name = sys.argv[1]

        with open(file_name, "r") as file:
            contents = file.read()
        
    except FileNotFoundError as e:
        print(f"File error: {e}")
        return
            
    print(f"First 5 words: {get_word_range(contents, 0, 5)}")
    print(f"Last 5 words: {get_word_range(contents, -5, 0)}")
    print(f"7th through 10ths word: {get_word_range(contents, 6, 10)}")

if __name__ == "__main__":
    main()