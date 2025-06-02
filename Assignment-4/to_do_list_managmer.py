tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else "✗"
        print(f"{i}. {task['task']} [{status}]")

def add_task():
    task_text = input("Enter new task: ")
    tasks.append({"task": task_text, "done": False})

def remove_task():
    show_tasks()
    index = int(input("Enter task number to remove: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
    else:
        print("Invalid task number.")

def mark_complete():
    show_tasks()
    index = int(input("Enter task number to mark as complete: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
    else:
        print("Invalid task number.")

def update_task():
    show_tasks()
    index = int(input("Enter task number to update: ")) - 1
    if 0 <= index < len(tasks):
        new_text = input("Enter new task text: ")
        tasks[index]["task"] = new_text
    else:
        print("Invalid task number.")

while True:
    print("\nTo-Do List Manager:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Update task")
    print("5. Mark task as complete")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        update_task()
    elif choice == "5":
        mark_complete()
    elif choice == "6":
        break
    else:
        print("Invalid choice.")
