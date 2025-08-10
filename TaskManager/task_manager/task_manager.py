"""
Task Manager Module

Contains the TaskManager class for creating, viewing, editing, deleting, 
and marking tasks as completed. Tasks are saved to and loaded from a JSON file.
"""

import json
import os

class TaskManager:
    """A simple task management system with JSON persistence."""

    def __init__(self):
        base_dir = os.path.dirname(__file__)  # Folder where this file lives
        self.filename = os.path.join(base_dir, "tasks.json")
        self.tasks = self.load_task()

    def load_task(self):
        """Load tasks from the JSON file in the module folder."""
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Error loading tasks: {e}")
            return []

    def save_task(self):
        """Save current tasks to the JSON file in the module folder."""
        try:
            with open(self.filename, "w") as f:
                json.dump(self.tasks, f, indent=4)
            print("✔ Changes saved successfully!")
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def add_task(self):
        """Prompt the user for task details and add it to the list."""
        while True:
            try:
                print("\nAdding new Task...")
                title = input("Enter title of task: ").strip().title()
                description = input("Enter description of task: ").strip()
                due_date = input("Enter the Due Date (DD/MM): ").strip()

                task = {
                    "title": title,
                    "description": description,
                    "due_date": due_date,
                    "status": "Pending"
                }
                self.tasks.append(task)
                print("✔ Task added successfully.")

                again = input("Do you want to add another task? (y/n): ").strip().lower()
                if again != "y":
                    break
            except Exception as e:
                print(f"Error adding task: {e}")

    def list_task(self):
        """Display all tasks."""
        print("\nList of All Tasks\n")
        if not self.tasks:
            print("No tasks to show!\n")
            return

        for idx, task in enumerate(self.tasks, 1):
            print("-" * 40)
            print(f"Task No: {idx}")
            print(f"Title      : {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Due Date   : {task['due_date']}")
            print(f"Status     : {task['status']}")
            print("-" * 40, "\n")

    def get_task_index(self, prompt):
        """Ask the user for a task number and return its index or None if invalid."""
        try:
            index = int(input(prompt)) - 1
            if 0 <= index < len(self.tasks):
                return index
            print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
        return None

    def mark_task(self):
        """Mark a task as completed."""
        self.list_task()
        if not self.tasks:
            return

        index = self.get_task_index("Enter the task number to mark as completed: ")
        if index is not None:
            self.tasks[index]['status'] = "✔ Completed"
            print(f"Task '{self.tasks[index]['title']}' marked as completed.")

    def delete_task(self):
        """Delete a selected task."""
        self.list_task()
        if not self.tasks:
            return

        index = self.get_task_index("Enter the task number to delete: ")
        if index is not None:
            removed = self.tasks.pop(index)
            print(f"Task '{removed['title']}' removed successfully.")

    def edit_task(self):
        """Edit details of a selected task."""
        while True:
            self.list_task()
            if not self.tasks:
                print("No task to edit.")
                return

            index = self.get_task_index("Enter task number to edit: ")
            if index is None:
                return

            task = self.tasks[index]
            task['title'] = input(f"Enter new title [{task['title']}]: ").strip().title() or task['title']
            task['description'] = input(f"Enter new description [{task['description']}]: ").strip() or task['description']
            task['due_date'] = input(f"Enter new Due Date (DD/MM) [{task['due_date']}]: ").strip() or task['due_date']
            task['status'] = input(f"Enter new status [{task['status']}]: ").strip().capitalize() or task['status']

            print(f"Task '{task['title']}' updated successfully.")

            again = input("Do you want to update another task? (y/n): ").lower().strip()
            if again != "y":
                break
