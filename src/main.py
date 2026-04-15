import csv
from datetime import datetime

def add_task():
    task = input("Task: ")
    deadline = input("Deadline (YYYY-MM-DD): ")
    status = "Pending"

    with open('data/tasks.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([task, deadline, status])

    print("Task added!")

def view_tasks():
    with open('data/tasks.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def check_overdue():
    today = datetime.today().date()

    with open('data/tasks.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == "deadline":
                continue
            deadline = datetime.strptime(row[1], "%Y-%m-%d").date()
            if deadline < today and row[2] == "Pending":
                print("Overdue:", row[0])

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Check Overdue\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        check_overdue()
    else:
        break
