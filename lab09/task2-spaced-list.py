def main():
    print("Statistics on list of words")
    line = input('Input space separated list of words: ')
    words = list(filter(lambda word: word, line.split(" ")))
    count_map = {}
    for word in words:
        if not word in count_map:
            count_map[word] = 0
        count_map[word] += 1

    non_repeating_words = list(filter(lambda key: count_map[key] == 1, count_map.keys()))

    print(f"Words: {words}\nLength: {len(words)}\nUnique words: {list(set(words))}\nOnly occur once: {non_repeating_words}")

if __name__ == "__main__":
    main()