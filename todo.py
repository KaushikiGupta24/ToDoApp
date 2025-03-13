import json
import os

TODO_FILE = "tasks.json"

def load_tasks():
    """Load tasks from a file."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to a file."""
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    """Add a new task."""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"Task added: {task}")

def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for i, t in enumerate(tasks, 1):
            status = "✔" if t["done"] else "❌"
            print(f"{i}. {t['task']} [{status}]")

def mark_done(task_number):
    """Mark a task as done."""
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        print(f"Task marked as done: {tasks[task_number - 1]['task']}")
    else:
        print("Invalid task number.")

def remove_task(task_number):
    """Remove a task."""
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Removed task: {removed_task['task']}")
    else:
        print("Invalid task number.")

def show_help():
    """Display help message."""
    print("\nTo-Do List CLI Commands:")
    print("  add <task>       - Add a new task")
    print("  list             - List all tasks")
    print("  done <task_no>   - Mark a task as done")
    print("  remove <task_no> - Remove a task")
    print("  help             - Show available commands")
    print("  exit             - Exit the program\n")

def main():
    """Main function to handle user commands."""
    show_help()
    while True:
        command = input("\nEnter command: ").strip().split(" ", 1)
        action = command[0].lower()

        if action == "add" and len(command) > 1:
            add_task(command[1])
        elif action == "list":
            list_tasks()
        elif action == "done" and len(command) > 1 and command[1].isdigit():
            mark_done(int(command[1]))
        elif action == "remove" and len(command) > 1 and command[1].isdigit():
            remove_task(int(command[1]))
        elif action == "help":
            show_help()
        elif action == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid command. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()
