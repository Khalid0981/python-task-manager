# 📝 Task Manager (Python CLI)

A simple command-line **Task Manager** built in Python, allowing you to add, view, edit, delete, and mark tasks as completed.  
Tasks are stored in a **JSON file** so they persist between program runs.

---

## 🚀 Features
- Add new tasks with title, description, and due date
- View all tasks in a clean list format
- Mark tasks as completed
- Edit existing tasks (with option to keep existing values)
- Delete tasks
- Automatic saving/loading from `tasks.json`

---

## 📂 Project Structure
task-manager/
│
├── task_manager.py # Core TaskManager class
├── main.py # CLI interface
├── tasks.json # Stored tasks (auto-generated)
└── README.md # Project documentation