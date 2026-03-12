# Shopping Cart System

A simple command-line shopping cart application built in Python that allows users to purchase products, validate inputs, and view a detailed purchase summary.

## Project Overview

This project implements an interactive shopping system where users can add multiple products to their cart and receive a complete summary of their purchase including total costs.

## File Structure

### 1. **main.py**
- **Purpose**: Entry point of the application
- **Functionality**: 
  - Imports the `ContinueShopping` function from `continue_shopping.py`
  - Initializes the shopping session

### 2. **continue_shopping.py**
- **Purpose**: Main shopping loop and user interaction handler
- **Key Features**:
  - Displays a prompt asking if the user wants to buy something
  - Collects product information by calling `record_sales()` function
  - Maintains a purchase history list of all transactions
  - Displays a comprehensive purchase summary with:
    - Product details (name, unit price, quantity)
    - Item totals (price × quantity)
    - Final total amount to pay
  - Handles invalid input gracefully with error messages
- **Main Function**: `ContinueShopping()`

### 3. **record_sales.py**
- **Purpose**: Product data input collection and validation
- **Key Features**:
  - **Product Name Validation**: 
    - Ensures the name is not empty
    - Continuously prompts until valid input is provided
  - **Price Validation**:
    - Converts input to float
    - Prevents negative prices
    - Handles invalid numeric input with error messages
  - **Quantity Validation**:
    - Converts input to integer
    - Prevents negative quantities
    - Handles invalid numeric input with error messages
  - **Calculation**: Computes total price (price × quantity)
  - **Return Value**: Tuple containing `(name, price, quantity, total_price)`
- **Main Function**: `record_sales()`

## How It Works

1. **Start Application**: Run `python main.py`
2. **Shopping Loop**:
   - User is prompted: "Do you want to buy something? (yes/no):"
   - If **"yes"**: 
     - User enters product name
     - User enters product price
     - User enters quantity desired
     - Product is added to purchase history
   - If **"no"**: Shopping ends and summary is displayed
   - If invalid input: Error message appears and user is prompted again
3. **Purchase Summary**:
   - All items are listed with their details
   - Final total is calculated and displayed
   - Thank you message is shown

## Usage Example

```
Do you want to buy something? (yes/no): yes
Enter the product name: Laptop
Enter the product price: 999.99
How many products do you want to buy?: 2
Product registered successfully.
Do you want to buy something? (yes/no): yes
Enter the product name: Mouse
Enter the product price: 25.50
How many products do you want to buy?: 3
Product registered successfully.
Do you want to buy something? (yes/no): no

--- PURCHASE SUMMARY ---
Product: Laptop | Unit Price: 999.99 | Quantity: 2 | Total to pay: 1999.98
Product: Mouse | Unit Price: 25.5 | Quantity: 3 | Total to pay: 76.5
------------------------------
FINAL TOTAL TO PAY: $ 2076.48
Thank you for your purchase, come back soon
```

## Installation & Requirements

- **Python Version**: Python 3.x
- **Dependencies**: None (uses only standard library)
- **Installation**: No additional setup required

## Running the Application

```bash
python main.py
```

## Input Validation Rules

- **Product Name**: Cannot be empty
- **Price**: Must be a positive number (integer or decimal)
- **Quantity**: Must be a positive integer
- All validation includes error handling with user-friendly messages

## Technical Details

- **Data Structure**: Purchase history is maintained as a list of tuples
- **Input Handling**: All user inputs are validated with try-except blocks for type conversion
- **Error Recovery**: Invalid inputs trigger error messages and re-prompt the user
- **Calculation**: All arithmetic is performed using floating-point numbers for accurate pricing

## Notes

- The application continues indefinitely until the user selects "no"
- All currency values are displayed without currency symbols for flexibility
- The `.lower().strip()` methods ensure case-insensitive input and remove whitespace
