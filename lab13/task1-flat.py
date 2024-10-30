import random

class Flat:
    __number = 0
    __owner = ""
    __square = 0.0
    __price = 0.0

    def __init__(self, number: int, owner: str, square: float, price: float):
        self.__number = number
        self.__owner = owner
        self.__square = square
        self.__price = price

    def set_price(self, price: float):
        self.__price = price

    def __str__(self):
        return f"Flat no. {self.__number} of {round(self.__square)} m² owned by {self.__owner} and costs {round(self.__price, 2)}$"

def main():
    print("Real estate database")
    owners = ['Sergiy P', 'Vitalii B', 'Anna P', 'Alesia T', 'Igor M', 'Mykyta B']

    flats: list[Flat] = []
    for i in range(random.randint(10, 20)):
        flats.append(Flat(i + 1, owners[random.randint(0, len(owners) - 1)], 30 + random.random() * 150, 10000 + random.random() * 20000))

    print(f"Flats generated:")
    for flat in flats:
        print(flat)

    while True:
        no = input("Input the flat no you want to trade (or leave empty to exit): ")
        if not no:
            return
        
        try:
            number = int(no)
            if (number < 1 or number > len(flats)):
                raise ValueError("Must be an existing flat number")
            
            flat = flats[number - 1]
            
            price = float(input("Input new price: "))
            if (price <= 0):
                raise ValueError("Must be a positive number")
        
            flat.set_price(price)
            
            print(f"Updated flats state:")
            for flat in flats:
                print(flat)
                
        except ValueError as e:
            print(f"Input error: {e}")
            continue
            
if __name__ == "__main__":
    main()