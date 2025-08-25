def task():
    task=[]
    print("=================Welcome to Task Management System=================")

    total_task=int(input("Enter the total number of tasks you want to complete: "))
    for i in range(0,total_task):
        task_name=input("Enter the name of the task: ")
        task.append(task_name)
    print("Tasks added successfully!")