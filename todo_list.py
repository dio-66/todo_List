class ToDoList:
    # Initialize an empty list to store tasks
    def __init__(self):
        self.tasks = []

    def add_task(self):
        # Prompt user to enter a new task
        task = input("Enter a new task: ")
        # Add the task to the list
        self.tasks.append(task)
        print("Task added successfully!")

    def remove_task(self):
        # Check if the list is empty
        if not self.tasks:
            print("No tasks found!")
            return

        # Display the current tasks
        self.view_tasks()
        # Prompt user to enter the number of the task to remove
        index = int(input("Enter the number of the task to remove: ")) - 1
        # Check if the index is within a valid range
        if 0 <= index < len(self.tasks):
            # Remove the task from the list
            removed_task = self.tasks.pop(index)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number!")

    def view_tasks(self):
        # Check if the list is not empty
        if self.tasks:
            print("Tasks:")
            # Iterate over the tasks with their corresponding numbers
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks found!")

    def start(self):
        while True:
            print("\n=== To-Do List ===")
            print("1. Add Task")
            print("2. Remove Task")
            print("3. View Tasks")
            print("4. Quit")

            # Prompt user to enter their choice
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.add_task()  # Call the add_task method
            elif choice == '2':
                self.remove_task()  # Call the remove_task method
            elif choice == '3':
                self.view_tasks()  # Call the view_tasks method
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Create an instance of the ToDoList class
todo = ToDoList()

# Start the to-do list application
todo.start()
