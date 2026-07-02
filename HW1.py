

# H1) Amazon Fulfillment Centre

# An Amazon fulfillment centre has a conveyor belt with exactly 8 slots numbered 0–7. Each slot holds one product. The warehouse manager needs to:

# Check what's at a slot
# Find a product
# Update a slot
# Check if the belt is full

# The conveyor belt has fixed 8 slots.
#===================================================================================================================================================
belt = ["Empty"] * 8

while True:
    print("\n1. Update Slot")
    print("2. Check Slot")
    print("3. Find Product")
    print("4. Check Belt Full")
    print("5. Display Belt")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        slot = int(input("Enter slot (0-7): "))
        if 0 <= slot < 8:
            product = input("Enter product name: ")
            belt[slot] = product
        else:
            print("Invalid slot!")

    elif choice == 2:
        slot = int(input("Enter slot (0-7): "))
        if 0 <= slot < 8:
            print("Product:", belt[slot])
        else:
            print("Invalid slot!")

    elif choice == 3:
        product = input("Enter product to find: ")
        if product in belt:
            print("Found at slot", belt.index(product))
        else:
            print("Product not found!")

    elif choice == 4:
        if "Empty" in belt:
            print("Belt is NOT Full")
        else:
            print("Belt is Full")

    elif choice == 5:
        for i in range(8):
            print(f"Slot {i}: {belt[i]}")

    elif choice == 6:
        break

    else:
        print("Invalid choice!")