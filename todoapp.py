
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
    