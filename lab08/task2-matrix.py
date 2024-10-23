import numpy as np
import random

def main():
    matrix_height = 3
    matrix_width = 4

    print("Rearranging the matrix")
    try:
        a = int(input('Input a: '))
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    matrix_m = np.zeros((matrix_height, matrix_width))
    for i in range(matrix_height):
        for j in range(matrix_width):
            matrix_m[i][j] = random.randint(-a, a)

    print(f"Matrix generated:\n{matrix_m}")
    
    max_elem = -a
    for i in range(matrix_height):
        for j in range(matrix_width):
            if matrix_m[i][j] > max_elem:
                max_elem = matrix_m[i][j]

    for i in range(matrix_height):
        for j in range(matrix_width):
            if matrix_m[i][j] == 0:
                matrix_m[i][j] = max_elem

    [line0, line1, line2] = matrix_m 

    print(f"Lines of the transformed matrix:\n{line0}\n{line1}\n{line2}")
    
if __name__ == "__main__":
    main()