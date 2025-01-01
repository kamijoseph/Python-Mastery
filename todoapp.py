
# Python To do List App with JSON
import json

# Storage file
FILE_NAME = "tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)
        
def display_tasks(tasks):
    if not tasks:
        print("No Tasks Available!")
    else:
        print("\nTo-Do List:")