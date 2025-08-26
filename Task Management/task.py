def task():
    task=[]
    print("=================Welcome to Task Management System=================")

    total_task=int(input("Enter the total number of tasks you want to complete: "))
    for i in range(0,total_task):
        task_name=input(f"Enter the task {i+1}: ")
        task.append(task_name)
    print("Tasks added successfully!")

    while True:
        option=int(input("Choose an option:\n1. Add Tasks\n2. Update Task\n3. Delete Task\n4. View Tasks\n5. Exit\n"))
        if option==1:
            new_task=input("Enter the new task: ")
            task.append(new_task)
            print(f"Task '{new_task}' added successfully!")
        elif option==2:
            update_task=input("Enter the number of the task you want to update: ")
            if update_task in task:
                new_name=input("Enter the new name for the task: ")
                ind=task.index(update_task)
                task[ind]=new_name
                print(f"Task '{update_task}' updated successfully!")
            else:
                print(f"Task '{update_task}' not found!")
