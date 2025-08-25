def task():
    task=[]
    print("=================Welcome to Task Management System=================")

    total_task=int(input("Enter the total number of tasks you want to complete: "))
    for i in range(0,total_task):
        task_name=input("Enter the name of the task: ")
        task.append(task_name)
    print("Tasks added successfully!")

    while True:
        option=int(input("Choose an option:\n1. Add Tasks\n2. Update Task\n3. Delete Task\n4. View Tasks\n5. Exit\n"))