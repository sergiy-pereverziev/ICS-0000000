import os, sys, requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def main():
    print("Find URLs with given extensions")

    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <extensions_list_file_name>")
        return

    try:
        file_name = sys.argv[1]

        with open(file_name, "r") as file:
            contents = file.read()
            extensions = contents.split("\n")
        
    except FileNotFoundError as e:
        print(f"File error: {e}")
        return
            
    print(f"Extensions parsed: {extensions}")
    
    while True:
        url = input("Input target URL (or leave empty to exit): ")
        if not url:
            return
        
        try:
            result = requests.get(url)
            if result.status_code != 200:
                raise RuntimeError(f"Could not load from {url}")
            
            page = BeautifulSoup(result.text, 'html.parser')

            links = []
            for image in page.find_all("img"):
                if not 'src' in image.attrs:
                    continue

                path = urlparse(image.attrs['src']).path
                ext = os.path.splitext(path)[1][1:]

                if ext in extensions:
                    links.append(image.attrs['src'])

            if len(links):
                print(f"Links found:\n{"\n".join(links)}")
            else:
                print("No links found")

        except Exception as e:
            print(f"Error: {e}")
            continue

if __name__ == "__main__":
    main()