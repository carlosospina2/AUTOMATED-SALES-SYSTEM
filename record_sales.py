
def record_sales():
    name_valid = True
    while name_valid:
        name = input("Enter the product name: ").strip()
        if name == "":
            print("ERROR! Name cannot be empty.")
        else:
            name_valid = False 

    price_valid = True
    while price_valid:
        try:
            price = float(input("Enter the product price: "))
            if price < 0:
                int("Force Error") 
            else:
                price_valid = False 
        except ValueError:
            print("ERROR! Invalid price (must be a positive number). Try again.")

    quantity_valid = True
    while quantity_valid:
        try:
            quantity = int(input("How many products do you want to buy?: "))
            if quantity < 0:
                int("Force Error")
            else:
                quantity_valid = False 
        except ValueError:
            print("ERROR! Invalid quantity (must be a positive integer). Try again.")

    total_price = price * quantity
    return (name, price, quantity, total_price)