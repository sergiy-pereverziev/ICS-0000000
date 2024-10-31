import sys, requests, numpy, re

def main():
    print("Parsing keywords in a webpage")

    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <urls_list_file_name>")
        return

    try:
        file_name = sys.argv[1]

        with open(file_name, "r") as file:
            contents = file.read()
            urls = list(filter(len, contents.split("\n")))
            if not len(urls):
                print("Empty list of URLs")
                return
        
    except FileNotFoundError as e:
        print(f"File error: {e}")
        return
    
    keywords = []
            
    while True:
        keyword = input("Input keyword (or leave empty to run search): ")
        if not keyword:
            if not len(keywords):
                print("Please input at least one keyword")
                continue
            break

        keywords.append(keyword)

    keyword_usage = dict(zip(keywords, map(int, numpy.zeros(len(keywords)))))
        
    for url in urls:
        try:
            result = requests.get(url)
            if result.status_code != 200:
                raise RuntimeError(f"Could not load from {url}")
                        
            for keyword in keywords:
                keyword_usage[keyword] += len(re.findall(r'\b' + keyword + r'\b', result.text, re.RegexFlag.I))

        except Exception as e:
            print(f"Error: {e}")
            continue

    print("Total occurences by keyword:")
    print("\n".join(list(map(lambda key: f"{key}: {keyword_usage[key]}", keyword_usage.keys()))))

if __name__ == "__main__":
    main()