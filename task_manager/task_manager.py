"""
Task Manager - A simple CLI app for managing tasks.
Tasks persist between sessions by saving to tasks.json
"""

import json
import os

class Task:
    """A single task with a description and completion status."""

    def __init__(self, description, completed=False):
        """Create a new task."""
        self.description = description
        self.completed = completed

    def mark_completed(self):
        """Mark this task as done."""
        self.completed = True 

    def __str__(self):
        """Return a readable string representation of the task."""
        status = "✓" if self.completed else "○"
        return f"{status} {self.description}"

TASKS_FILE = "tasks.json"


def save_tasks(tasks):
    """Save the list of tasks to a JSON file."""
    # Convert each Task object to a dictionary
    tasks_data = [
        {"description": t.description, "completed": t.completed}
        for t in tasks
    ]

    with open(TASKS_FILE, "w") as f:
        json.dump(tasks_data, f, indent=2)


def load_tasks():
        """Load tasks from the JSON file. Returns an empty list if file doesn't exist."""
        if not os.path.exists(TASKS_FILE):
            return []
    
        with open(TASKS_FILE, "r") as f:
            tasks_data = json.load(f)
    
        # Convert each dictionary back to a Task object
        return [Task(d["description"], d["completed"]) for d in tasks_data]

def main():
    """Main program loop."""
    print("=== Task Manager ===")
    tasks = load_tasks()
    
    while True:
        # Show the menu
        print("\n1. Add task")
        print("2. List tasks")
        print("3. Mark task complete")
        print("4. Delete task")
        print("5. Quit")
        
        choice = input("\nChoose an option: ").strip()
        
        if choice == "1":
            description = input("Task description: ").strip()
            if description:
                tasks.append(Task(description))
                save_tasks(tasks)
                print(f"Added: {description}")
            else:
                print("Task cannot be empty.")
        
        elif choice == "2":
            if not tasks:
                print("No tasks yet.")
            else:
                print("\nYour tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
        
        elif choice == "3":
            if not tasks:
                print("No tasks to mark.")
                continue
            
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            
            try:
                num = int(input("Number to mark complete: "))
                if 1 <= num <= len(tasks):
                    tasks[num - 1].mark_completed()
                    save_tasks(tasks)
                    print("Marked complete.")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a number.")
        
        elif choice == "4":
            if not tasks:
                print("No tasks to delete.")
                continue
            
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            
            try:
                num = int(input("Number to delete: "))
                if 1 <= num <= len(tasks):
                    deleted = tasks.pop(num - 1)
                    save_tasks(tasks)
                    print(f"Deleted: {deleted.description}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a number.")
        
        elif choice == "5":
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Choose 1-5.")

if __name__ == "__main__":
    main()