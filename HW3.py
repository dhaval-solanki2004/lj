# H3) The GPS Navigation System (Backtracking)
# You're building a GPS app like Google Maps for a hiking trail. The hiker moves through checkpoints. If they take a wrong turn, they hit "Go Back" to return to the previous checkpoint. But once they go back, they can also "Go Forward" if they change their mind again — just like a browser's back/forward buttons.
# Operations:
# visit(place) — move to a new place
# back() — go to previous place
# forward() — go forward if available


back_stack = []
forward_stack = []
current = "Home"

while True:
    print("\n1. Visit Place")
    print("2. Go Back")
    print("3. Go Forward")
    print("4. Current Location")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        place = input("Enter place: ")
        back_stack.append(current)
        current = place
        forward_stack.clear()

    elif choice == 2:
        if back_stack:
            forward_stack.append(current)
            current = back_stack.pop()
        else:
            print("No previous location")

    elif choice == 3:
        if forward_stack:
            back_stack.append(current)
            current = forward_stack.pop()
        else:
            print("No forward location")

    elif choice == 4:
        print("Current Location:", current)

    elif choice == 5:
        break

    else:
        print("Invalid choice")