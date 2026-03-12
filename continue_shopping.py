from record_sales import record_sales 

def ContinueShopping():    
    purchase_history = []
    running = True

    while running:
        answer = input("Do you want to buy something? (yes/no): ").strip().lower()

        if answer == "yes":
            product_data = record_sales()
            purchase_history.append(product_data)
            print("Product registered successfully.")

        elif answer == "no":
            print("\n--- PURCHASE SUMMARY ---")
            final_total = 0

            for item in purchase_history:
                print(f"Product: {item[0]} | Unit Price: {item[1]} | Quantity: {item[2]} | Total to pay: {item[3]}")
                final_total = final_total + item[3]

            print("-" * 30)
            print("FINAL TOTAL TO PAY: $", final_total)
            print("Thank you for your purchase, come back soon")
            running = False

        else:
            print("ERROR!!! Only enter yes or no")