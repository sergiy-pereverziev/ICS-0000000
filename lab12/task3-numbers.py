import digit_analysis as da

def main():
    print("Analyzing numbers")
    for (number, expected_result) in [(1, True), (11, True), (13, False), (121, True), (122, False), (131, True), (13234843231, True), (1234843231, False)]:
        actual_result = da.is_palindrome(number)
        print(f"Number: {number} is a palyndrome: {expected_result} while is_palinrome returns {actual_result}")
        if actual_result != expected_result:
            raise AssertionError("Mismatch!")
        
    for (number, expected_result) in [(11, 0), (121, 0), (132, 1), (313, 0), (413, -1), (4004, 0), (1009, 1), (9911, -1)]:
        actual_result = da.compare_edge_digits(number)
        print(f"Number {number}'s last digit is {"same as" if expected_result == 0 else "less than" if expected_result == -1 else "greater than"} the first one while compare_edge_digits says it's {"same" if actual_result == 0 else "less" if actual_result == -1 else "greater"}")
        if actual_result != expected_result:
            raise AssertionError("Mismatch!")    
        
if __name__ == "__main__":
    main()