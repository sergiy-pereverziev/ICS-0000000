import sys

def main():
    result_unique_filename = "unique.txt"
    result_duplicates_filename = "duplicates.txt"
    result_commas_count_filename = "commas-count.txt"

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
            
    clean_words = list(map(lambda word: word.strip(","), filter(lambda word: word, " ".join(contents.split("\n")).split(" "))))
    unique = sorted(list(set(clean_words)))
    count_map = {}
    for word in clean_words:
        if not word in count_map:
            count_map[word] = 0
        count_map[word] += 1

    words_occurring_twice = filter(lambda key: count_map[key] == 2, count_map.keys())
    commas_count = len(list(filter(lambda sym: sym == ",", contents)))

    open(result_unique_filename, "w").write(" ".join(unique))
    open(result_duplicates_filename, "w").write(" ".join(words_occurring_twice))
    open(result_commas_count_filename, "w").write(str(commas_count))

if __name__ == "__main__":
    main()