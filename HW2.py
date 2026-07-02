# H2) Toll Plaza Simulation (Circular Queue)
# A toll plaza has a fixed capacity of 5 vehicles. If full, new vehicles must wait.
# Implement a Circular Queue to simulate this, since it reuses empty slots without wasting memory.

MAX = 5
queue = [None] * MAX
front = -1
rear = -1

while True:
    print("\n1. Enqueue Vehicle")
    print("2. Dequeue Vehicle")
    print("3. Display Queue")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        vehicle = input("Enter vehicle number: ")

        if (rear + 1) % MAX == front:
            print("Queue is Full")

        else:
            if front == -1:
                front = rear = 0
            else:
                rear = (rear + 1) % MAX

            queue[rear] = vehicle
            print("Vehicle Added")

    elif choice == 2:
        if front == -1:
            print("Queue is Empty")

        else:
            print("Vehicle Left:", queue[front])

            if front == rear:
                front = rear = -1
            else:
                front = (front + 1) % MAX

    elif choice == 3:
        if front == -1:
            print("Queue is Empty")

        else:
            i = front
            while True:
                print(queue[i], end=" ")
                if i == rear:
                    break
                i = (i + 1) % MAX
            print()

    elif choice == 4:
        break

    else:
        print("Invalid Choice")
