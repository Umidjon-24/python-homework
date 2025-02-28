from abc import ABC, abstractmethod
import json
import csv
import os

# Task Model
class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Task(data["task_id"], data["title"], data["description"], data.get("due_date"), data["status"])

# Storage Interface
class Storage(ABC):
    @abstractmethod
    def save(self, tasks):
        pass
    
    @abstractmethod
    def load(self):
        pass

# CSV Storage
class CSVStorage(Storage):
    def __init__(self, filename):
        self.filename = filename
    
    def save(self, tasks):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["task_id", "title", "description", "due_date", "status"])
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())
    
    def load(self):
        if not os.path.exists(self.filename):
            return []
        tasks = []
        with open(self.filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append(Task.from_dict(row))
        return tasks

# JSON Storage
class JSONStorage(Storage):
    def __init__(self, filename):
        self.filename = filename
    
    def save(self, tasks):
        with open(self.filename, 'w') as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)
    
    def load(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as file:
            return [Task.from_dict(task) for task in json.load(file)]

# To-Do Application
class ToDoApp:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = self.storage.load()
    
    def add_task(self):
        task_id = input("Enter Task ID: ")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD) (optional): ") or None
        status = input("Enter Status (Pending/In Progress/Completed): ")
        self.tasks.append(Task(task_id, title, description, due_date, status))
        print("Task added successfully!")
    
    def view_tasks(self):
        for task in self.tasks:
            print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")
    
    def update_task(self):
        task_id = input("Enter Task ID to update: ")
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = input("Enter new Title: ") or task.title
                task.description = input("Enter new Description: ") or task.description
                task.due_date = input("Enter new Due Date (YYYY-MM-DD): ") or task.due_date
                task.status = input("Enter new Status (Pending/In Progress/Completed): ") or task.status
                print("Task updated successfully!")
                return
        print("Task not found!")
    
    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")
    
    def filter_tasks(self):
        status = input("Enter status to filter (Pending/In Progress/Completed): ")
        filtered_tasks = [task for task in self.tasks if task.status == status]
        for task in filtered_tasks:
            print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")
    
    def save_tasks(self):
        self.storage.save(self.tasks)
        print("Tasks saved successfully!")
    
    def run(self):
        while True:
            print("\nWelcome to the To-Do Application!")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.filter_tasks()
            elif choice == "6":
                self.save_tasks()
            elif choice == "7":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

# Select storage format
storage_type = input("Choose storage format (CSV/JSON): ").strip().lower()
storage = CSVStorage("tasks.csv") if storage_type == "csv" else JSONStorage("tasks.json")

todo_app = ToDoApp(storage)
todo_app.run()
