# Define a list to store tasks
tasks = []

# Function to add a task to the to-do list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the to-do list.")

# Function to view all tasks
def view_tasks():
    if tasks:
        print("To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks in the to-do list.")

# Function to mark a task as done
def mark_done(task_index):
    if 1 <= task_index <= len(tasks):
        task = tasks[task_index - 1]
        print(f"Task '{task}' marked as done.")
        tasks.pop(task_index - 1)
    else:
        print("Invalid task index. Please provide a valid task index.")

# Function to remove a task from the to-do list
def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        task = tasks[task_index - 1]
        print(f"Task '{task}' removed from the to-do list.")
        tasks.pop(task_index - 1)
    else:
        print("Invalid task index. Please provide a valid task index.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as done")
    print("4. Remove a task")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        task_index = int(input("Enter the index of the task to mark as done: "))
        mark_done(task_index)
    elif choice == "4":
        view_tasks()
        task_index = int(input("Enter the index of the task to remove: "))
        remove_task(task_index)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
