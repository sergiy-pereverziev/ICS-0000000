import sys

def main():
    # Check if exactly one arguments is passed (excluding the script name)
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <rib_length>")
        return

    try:
        # Read input from stdin
        rib_length_str = sys.argv[1]

        # Convert input to a float and validate it's a positive number
        try:
            rib_length = float(rib_length_str)
        except ValueError:
            raise ValueError("Rib length must be a valid positive number.")

        if rib_length <= 0:
            raise ValueError("Rib length must be a positive number.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    # Calculate and display the results
    volume = rib_length ** 3
    side_surface_area = 4 * (rib_length ** 2)

    print(f"Volume of the cube: {volume} meters")
    print(f"Side surface area of the cube: {side_surface_area} meters")

if __name__ == "__main__":
    main()
