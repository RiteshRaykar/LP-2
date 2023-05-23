stocks = {}

def buy_stock():
    stock_name = input("Enter the stock name: ")
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price per share: "))

    if stock_name in stocks:
        stocks[stock_name]["quantity"] += quantity
        stocks[stock_name]["average_price"] = (stocks[stock_name]["average_price"] + price) / 2
    else:
        stocks[stock_name] = {
            "quantity": quantity,
            "average_price": price
        }
    print(f"Bought {quantity} shares of {stock_name} at ${price} each.")

def sell_stock():
    stock_name = input("Enter the stock name: ")
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price per share: "))

    if stock_name in stocks:
        if stocks[stock_name]["quantity"] >= quantity:
            stocks[stock_name]["quantity"] -= quantity
            if stocks[stock_name]["quantity"] == 0:
                del stocks[stock_name]
            print(f"Sold {quantity} shares of {stock_name} at ${price} each.")
        else:
            print(f"Error: Not enough shares of {stock_name} to sell.")
    else:
        print(f"Error: You don't own any shares of {stock_name}.")

def show_portfolio():
    if stocks:
        print("Your current portfolio:")
        for stock_name, stock_data in stocks.items():
            print(f"{stock_name}: {stock_data['quantity']} shares at ${stock_data['average_price']} each")
    else:
        print("Your portfolio is empty.")

def display_menu():
    print("----- Stock Trading System -----")
    print("1. Buy Stock")
    print("2. Sell Stock")
    print("3. Show Portfolio")
    print("4. Exit")

def process_choice(choice):
    if choice == "1":
        buy_stock()
    elif choice == "2":
        sell_stock()
    elif choice == "3":
        show_portfolio()
    elif choice == "4":
        print("Exiting...")
        return True
    else:
        print("Invalid choice. Please try again.")
    return False

# Main program loop
while True:
    display_menu()
    user_choice = input("Enter your choice (1-4): ")
    if process_choice(user_choice):
        break
