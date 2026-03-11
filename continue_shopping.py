from record_sales import record_sales

def continue_shopping():    
    list = []
    run = True
    while run:
        opcion = input("Do you want to buy something? (yes/no): ")
        if opcion == "yes":
            item = record_sales()
            list.append(item)
            print("Product successfully registered.")
        elif opcion == "no":
            print("\n--- SUMMARY OF YOUR PURCHASE ---")
            total_ending = 0
            for i in list:
                print(f"Product: {i[0]} | Unit price: {i[1]} | Amount: {i[2]} | Total to pay: {i[3]}")
                total_ending = total_ending + i[3]
            print("-" * 30)
            print("final total to pay: $", total_ending)
            print("Thank you for your purchase, Come back soon")
            run = False
        else:
            print("ERROR!!! Just enter yes o no")