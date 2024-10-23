import numpy as np
import random

def main():
    print("Collecting statistics on the array")
    
    lower = 3
    higher = 15
    length = 8

    vector_a = np.zeros(length)
    for i in range(len(vector_a)):
        vector_a[i] = random.randint(lower, higher)

    print(f"Vector generated: {vector_a}")
    
    vector_b = np.zeros(3)
    for n in vector_a:
        if n % 2 == 0:
            vector_b[0] += 1

        vector_b[2] += n

    vector_b[1] = len(vector_a) - vector_b[0]

    print(f"[Number of evens, Number of odds, Sum]: {vector_b}")
    
if __name__ == "__main__":
    main()