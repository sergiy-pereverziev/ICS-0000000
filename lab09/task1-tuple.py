def main():
    print("Unique values in a tuple")
    
    tuple = (100, "Elephant", "Ghost", 15.3, 16.48, 100, 1, "Ghost", 15.3, "Body")
    print(f"Tuple: {tuple}")

    unique = list(set(tuple))
    print(f"Unique values: {unique}")
    
if __name__ == "__main__":
    main()