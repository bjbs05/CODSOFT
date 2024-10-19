# Simple To-Do List program 

tasks = []

while True:
    print("\n1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")
    

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if tasks:
            print("\nYour tasks:")
            for task in tasks:
                print(f"- {task}")
        else:
            print("\nNo tasks in your list.")

    elif choice == "2":
        task = input("Enter the task to add: ")
        tasks.append(task)
        print(f"Task '{task}' added.")

    elif choice == "3":
        if tasks:
            task = input("Enter the task to remove: ")
            if task in tasks:
                tasks.remove(task)
                print(f"Task '{task}' removed.")
            else:
                print(f"Task '{task}' not found.")
        else:
            print("No tasks to remove.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
