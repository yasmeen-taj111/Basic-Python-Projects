print("Welcome to the FreshMart Grocery Shop")
print("-" * 50)

cart = {}

while True:
    print("\n1. Add Item to Cart")
    print("2. Delete Item from Cart")
    print("3. View Bill and Exit")

    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        item = input("Enter the item name: ").capitalize()
        qty = int(input(f"Enter the quantity of {item}: "))
        price = float(input(f"Enter the price of one {item}: ₹"))
        cart[item] = [qty, price]
        print(f"{item} added to cart!")

    elif choice == 2:
        item = input("Enter the item name to delete: ").capitalize()
        if item in cart:
            del cart[item]
            print(f"{item} removed from cart.")
        else:
            print("Item not found in cart.")

    elif choice == 3:
        print("\n" + "=" * 50)
        print("FINAL BILL - FreshMart Grocery Shop")
        print("=" * 50)
        total = 0
        print(f"{'Item':<15}{'Qty':<10}{'Price':<10}{'Total':<10}")
        print("-" * 50)
        for item, details in cart.items():
            qty, price = details
            item_total = qty * price
            total += item_total
            print(f"{item:<15}{qty:<10}{price:<10}{item_total:<10}")
        print("-" * 50)
        print(f"{'Grand Total':<35}₹{total:.2f}")
        print("=" * 50)
        print("Thank you for shopping with FreshMart!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
