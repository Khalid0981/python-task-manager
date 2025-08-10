"""
Task Manager CLI Application

This program allows users to add, view, edit, delete, and mark tasks as completed.
Tasks are automatically saved to a JSON file for persistence.
"""

from task_manager import TaskManager


def main():
    tm = TaskManager()  # Loads tasks automatically from JSON

    while True:
        try:
            print("\n=== Task Manager ===")
            print("1. Add a Task")
            print("2. View All Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete a Task")
            print("5. Edit a Task")
            print("6. Exit")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                tm.add_task()
                tm.save_task()
            elif choice == "2":
                tm.list_task()
            elif choice == "3":
                if tm.tasks:
                    tm.mark_task()
                    tm.save_task()
                else:
                    print("No tasks to mark.")
            elif choice == "4":
                if tm.tasks:
                    tm.delete_task()
                    tm.save_task()
                else:
                    print("No tasks to delete.")
            elif choice == "5":
                if tm.tasks:
                    tm.edit_task()
                    tm.save_task()
                else:
                    print("No tasks to edit.")
            elif choice == "6":
                print("Have a nice day!")
                break
            else:
                print("❌ Invalid choice. Please enter a number between 1 and 6.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
