import json
import csv

data = [
    {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
    {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
    {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
]

def save_file():
    with open('tasks.json', 'w') as file:
        json.dump(data, file, indent=4)

def load_file():
    with open('tasks.json', 'r') as file:
        data = json.load(file)
        return data
def statistics():
    total_tasks = len(data)
    completed_tasks = 0
    priority_sum = 0
    for i in range(len(data)):
        if data[i]['completed'] == True:
            completed_tasks += 1
        priority_sum += data[i]['priority']
    average_priority = priority_sum/total_tasks
    pending_tasks = total_tasks - completed_tasks
    print(f"Total tasks: {total_tasks}\nCompleted tasks: {completed_tasks}\nPending tasks: {pending_tasks}\nAverage priority: {average_priority}")

# statistics()

def to_csv():
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)    
    with open('tasks.csv', 'w', newline='') as f:   
        fieldnames = ['ID', 'Task Name', 'Completed Status', 'Priority']
        writer = csv.writer(f)
        writer.writerow(fieldnames)
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])

to_csv()