import json
import os


def add_to_do():
    task = input("Enter the task to be added into the to-do List: ")
    date = input("Enter the date as YYYY-MM-DD: ")
    times = input("Enter the Time as HH:MM:SS: ")
    status = input("Is the Task done? \"y\" for yes or \"n\" for not yet: ")
    status = status.lower() == "y"

    toDoList = {
        "Task": task,
        "Date": date,
        "Time": times,
        "Status": status
    }

    # Use 'with' to open the file
    with open("toDoList.json", "a+", encoding="UTF-8") as toDo:
        toDo.write(json.dumps(toDoList) + "\n")


def read_to_do():
    if not os.path.exists('toDoList.json'):
        print("No to-do list found.")
        return

    with open('toDoList.json', 'r', encoding="UTF-8") as f:
        for line in f:
            toDolist = json.loads(line)
            status_display = "Done" if toDolist["Status"] else "Not done yet"
            print(
                f"Task: {toDolist['Task']}, Date: {toDolist['Date']}, Time: {toDolist['Time']}, Status: {status_display}")


def update_status(task_name: str):
    updated = False
    tasks = []

    # Read existing tasks
    if os.path.exists('toDoList.json'):
        with open('toDoList.json', 'r', encoding="UTF-8") as f:
            for line in f:
                toDolist = json.loads(line)
                if toDolist["Task"] == task_name:
                    toDolist["Status"] = not toDolist["Status"]  # Toggle status
                    updated = True
                tasks.append(toDolist)

    # Write tasks back to the file
    with open('toDoList.json', 'w', encoding="UTF-8") as f:
        for task in tasks:
            f.write(json.dumps(task) + "\n")

    if updated:
        print(f"Status updated for task: {task_name}")
    else:
        print(f"No task found with the name: {task_name}")


def main():
    while True:
        print("Please choose from the following menu:")
        print("(1) Would you like to add to the to do list")
        print("(2) Would you like to view the to do list")
        print("(3) Would you like to update the status of a task")
        print("(7) To exit")
        userChoice = int(input("What would you like to do?   "))

        if userChoice == 1:
            add_to_do()
        elif userChoice == 2:
            read_to_do()
        elif userChoice == 3:
            user_input = input("Which task would you like to change the status for? ")
            update_status(user_input)
        elif userChoice == 7:
            break
        else:
            print("Invalid input! Please choose a number from the list!")


print("Welcome to the To Do list program")
main()