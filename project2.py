print("Welcome to Taj Restaurant")
print("-" * 50)

menu = {
    "Pasta": 120,
    "Burger": 80,
    "Pizza": 150,
    "Sandwich": 60,
    "Coffee": 50,
    "Ice Cream": 70
}

order = {}

print("\nToday's Menu:")
for dish, price in menu.items():
    print(f"{dish:<15} ₹{price}")

while True:
    print("\n1. Add Dish")
    print("2. Delete Dish")
    print("3. View Bill and Exit")

    ch = int(input("Enter your choice (1-3): "))

    if ch == 1:
        d = input("Enter dish name: ").capitalize()
        if d in menu:
            q = int(input(f"Enter quantity of {d}: "))
            order[d] = q
            print(f"{d} added to order.")
        else:
            print("Dish not available in menu.")

    elif ch == 2:
        d = input("Enter dish name to delete: ").capitalize()
        if d in order:
            del order[d]
            print(f"{d} removed from order.")
        else:
            print("Dish not found in order.")

    elif ch == 3:
        print("\n" + "=" * 50)
        print("FINAL BILL - Taj Restaurant")
        print("=" * 50)
        total = 0
        print(f"{'Dish':<15}{'Qty':<10}{'Price':<10}{'Total':<10}")
        print("-" * 50)
        for d, q in order.items():
            p = menu[d]
            amt = q * p
            total += amt
            print(f"{d:<15}{q:<10}{p:<10}{amt:<10}")
        tax = total * 0.05
        sc = total * 0.1
        g_total = total + tax + sc
        print("-" * 50)
        print(f"{'Subtotal':<35}₹{total:.2f}")
        print(f"{'Tax (5%)':<35}₹{tax:.2f}")
        print(f"{'Service Charge (10%)':<35}₹{sc:.2f}")
        print(f"{'Grand Total':<35}₹{g_total:.2f}")
        print("=" * 50)
        print("Thank you for dining with Taj Restaurant!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
