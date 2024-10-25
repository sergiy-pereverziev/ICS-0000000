import json, sys

def main():
    print("Searching on the JSON vehicle database")

    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <file_name>")
        return

    try:
        with open(sys.argv[1], 'r') as file:
            database = json.load(file)
    except FileNotFoundError as e:
        print(f"File error: {e}")
        return  
    except json.decoder.JSONDecodeError as e:
        print(f"JSON error: {e}")
        return
    
    available_colors = set(map(lambda item: item['color'], database))
    sorted_color_options = f'"{'", "'.join(sorted(available_colors))}"'

    while True:
        color = input(f"Input color ({sorted_color_options} or empty to exit): ")
        if not color:
            print("Empty input - exiting")
            break
        if not color in available_colors:
            print(f"Vehicles of {color} color not found. Available colors: {sorted_color_options}")
            continue

        result = list(map(lambda item: item['plate'], filter(lambda item: item['color'] == color, database)))

        print(f"{color.capitalize()} vehicle plate{"s" if len(result) > 1 else ""}: {', '.join(result)}")
        
if __name__ == "__main__":
    main()