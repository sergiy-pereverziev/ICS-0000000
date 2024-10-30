import math

def compare_edge_digits(number: int):
    string = str(number)
    first = int(string[0])
    last = int(string[-1])

    if first < last:
        return 1
    elif first > last:
        return -1
    else: 
        return 0
    
def is_palindrome(number: int):
    string = str(number)

    for i in range(math.floor(len(string) / 2)):
        if (string[i] != string[-i - 1]):
            return False
    
    return True