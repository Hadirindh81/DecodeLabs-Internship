# Project_1 To Do List Assignment Given by : DecodeLabs

tasks = []

while True:

    print("\n========== TO-DO LIST ==========")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Search for a task")
    print("4. Remove a task")
    print("5. Exit")
    print("================================")

    choice = input("Choose an option (1-5): ").strip()

    # ADD TASK
    if choice == "1":

        task = input("Enter a task: ").strip()

        if task:
            tasks.append(task)
            print("Task added successfully!")

        else:
            print("A task cannot be empty.")

    # VIEW ALL TASKS
    elif choice == "2":

        if len(tasks) == 0:
            print("Your to-do list is empty.")

        else:
            print("\n========== YOUR TASKS ==========")

            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

            print("================================")
            print(f"Total tasks: {len(tasks)}")

    # SEARCH TASK
    elif choice == "3":

        if len(tasks) == 0:
            print("Your to-do list is empty.")

        else:
            search_text = input(
                "Enter a word or phrase to search: "
            ).strip().lower()

            if not search_text:
                print("Search cannot be empty.")

            else:
                found = False

                print("\nSearch Results:")

                for number, task in enumerate(tasks, start=1):

                    if search_text in task.lower():
                        print(f"{number}. {task}")
                        found = True

                if not found:
                    print("No matching tasks found.")

    # REMOVE TASK
    elif choice == "4":

        if len(tasks) == 0:
            print("There are no tasks to remove.")

        else:
            print("\nYour Tasks:")

            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

            try:
                task_number = int(
                    input("Enter the task number to remove: ")
                )

                if 1 <= task_number <= len(tasks):

                    removed_task = tasks.pop(task_number - 1)

                    print(f"Removed successfully: {removed_task}")

                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    # EXIT
    elif choice == "5":

        print("Thank you for using To-Do List. Goodbye!")

        break

    else:

        print("Invalid choice! Please select between 1 and 5.")

