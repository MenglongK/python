def print_main_menu():
    print("========================================")
    print("         WELCOME TO OUR BAKERY          ")
    print("========================================")
    print("1. Order Items")
    print("2. View Total")
    print("3. Checkout")
    print("4. Exit")
    print("========================================")


def order_items(subtotal):
    print("=========BAKERY MENU=========")
    print("1. Croissant           $10.00")
    print("2. Chocolate Muffin    $2.50")
    print("3. Bread               $2.00")
    print("4. Back to Main Menu")
    print("=============================")

    item_choice = input("Select an item: ")

    match item_choice:
        case '1':
            subtotal += 10.00
            print("Croissant added successfully!")
            print(f"Current Subtotal: ${subtotal:.2f}")
        case '2':
            subtotal += 2.50
            print("Chocolate Muffin added successfully!")
            print(f"Current Subtotal: ${subtotal:.2f}")
        case '3':
            subtotal += 2.00
            print("Bread added successfully!")
            print(f"Current Subtotal: ${subtotal:.2f}")
        case '4':
            pass
        case _:
            print("Invalid item selection!")
            print("Subtotal remains unchanged.")
            print(f"Current Subtotal: ${subtotal:.2f}")

    return subtotal


def view_total(subtotal):
    print("=========YOUR ORDER=========")
    if subtotal == 0.0:
        print("Your order is empty")
    else:
        print(f"Current Subtotal: ${subtotal:.2f}")


def checkout(subtotal):
    print("=========CHECKOUT=========")
    if subtotal == 0.0:
        print("Your order is empty.")
        print("Please order something first.")
        return subtotal

    discount = 0.0
    if subtotal >= 10.00:
        discount = subtotal * 0.10
        print(f"Subtotal:           ${subtotal:.2f}")
        print(f"Discount (10%):     ${discount:.2f}")
    else:
        print(f"Subtotal:           ${subtotal:.2f}")
        print(f"Discount:           ${discount:.2f}")

    final_total = subtotal - discount
    print("--------------------------")
    print(f"Final Total:        ${final_total:.2f}")

    try:
        cash_received = float(input("Enter cash received ($): "))
        print("=========PAYMENT=========")

        if cash_received >= final_total:
            change = cash_received - final_total
            print(f"Final Total         ${final_total:.2f}")
            print(f"Cash Received       ${cash_received:.2f}")
            print(f"Change              ${change:.2f}")
            return 0.0
        else:
            shortage = final_total - cash_received
            print("Insufficient Payment!")
            print(f"You need ${shortage} more.")
            return subtotal

    except ValueError:
        print("=========PAYMENT=========")
        print("Invalid amount entered.")
        return subtotal


def main():
    subtotal = 0.0

    while True:
        print_main_menu()
        choice = input("Select an option: ")

        match choice:
            case '1':
                subtotal = order_items(subtotal)
            case '2':
                view_total(subtotal)
            case '3':
                subtotal = checkout(subtotal)
            case '4':
                print("Thank you for visiting our Bakery!")
                print("Have a wonderful day!")
                break
            case _:
                print("Invalid option! Please try again.")


if __name__ == "__main__":
    main()