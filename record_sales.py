def record_sales():
    state = True
    while state:  
        try:
            name = input("Enter the product name: ")  
            price = float(input("Enter the product price: "))
            amount = int(input("¿How many products do you want to buy?: "))
            subtotal = price * amount 
            state = False
            # We return the data as a tuple
            return (name, price, amount, subtotal)
        except ValueError:       
            print("¡ERROR! You must enter a number. Try again.")