
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
        for idx, task in enumerate(tasks, 1):
            status = "Done" if tasks["completed"] else "Pending"
            print(f"{idx}. {tasks['title']} [{status}]")

def add_tasks(tasks):
    title = input("Enter the title of the task: ")
    tasks.append({"title": title, "completed": False})
    print("Tasks Added Successfully!")
    
def mark_tasks_done(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("Enter The Task Number to be Marked: "))
        if 1 <= task_number <= len(tasks):
            tasks = [task_number - 1]["completed"] = True
            print("Tasks Marked as Done!")
        else:
            print("Invalid Task ")
    except ValueError:
        print("Please Enter a Valid Task Number!")

def delete_tasks(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("Enter The Task Number to be Deleted: "))
        if 1 <= task_number <= len(tasks):
            tasks.pop[task_number - 1]
            print("Task deleted Successfully.")
        else:
            print("Invalid Task!")
    except ValueError:
        print('Enter a Valid Task Number!')
        
def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- To-Do List App ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter Your Choice: ")
        if choice == '1':
            display_tasks(tasks)
        elif choice == "2":
            add_tasks(tasks)
        elif choice == "3":
            mark_tasks_done(tasks)
        elif choice == "4":
            delete_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("GoodBye.")
            break
        else:
            print("Invalid choice. Try Again.")


if __name__ == "__main__":
    main()