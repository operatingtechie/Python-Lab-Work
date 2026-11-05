inventory = {
    "Laptop": {"price": 50000, "quantity": 3},
    "Mouse": {"price": 500, "quantity": 10},
    "Keyboard": {"price": 1000, "quantity": 4}
}

while True:

    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. Update Quantity")
    print("3. Search Product")
    print("4. Calculate Total Inventory Value")
    print("5. Display Products with Quantity Below 5")
    print("6. Display All Products Sorted by Name")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter product name: ")

        if name in inventory:
            print("Product already exists!")
        else:
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))

            inventory[name] = {
                "price": price,
                "quantity": quantity
            }

            print("Product added successfully!")

    elif choice == "2":
        name = input("Enter product name: ")

        if name in inventory:
            quantity = int(input("Enter new quantity: "))
            inventory[name]["quantity"] = quantity
            print("Quantity updated successfully!")
        else:
            print("Product not found!")

    elif choice == "3":
        name = input("Enter product name: ")

        if name in inventory:
            print("Product Name:", name)
            print("Price:", inventory[name]["price"])
            print("Quantity:", inventory[name]["quantity"])
        else:
            print("Product not found!")

    elif choice == "4":
        total = 0

        for name in inventory:
            total += inventory[name]["price"] * inventory[name]["quantity"]

        print("Total Inventory Value:", total)

    elif choice == "5":
        print("Products with quantity below 5:")

        for name in inventory:
            if inventory[name]["quantity"] < 5:
                print(name, "- Quantity:", inventory[name]["quantity"])

    elif choice == "6":
        print("All Products (Sorted by Name):")

        for name in sorted(inventory):
            print(
                name,
                "| Price:", inventory[name]["price"],
                "| Quantity:", inventory[name]["quantity"]
            )

    elif choice == "7":
        print("Thank you for using Inventory Management System!")
        break

    else:
        print("Invalid choice! Please try again.")