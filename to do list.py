def show_tasks():
        try:
                with open("tasks.txt", "r") as file:
                        tasks = file.readlines()
                        if tasks:
                                print("Your tasks:")
                                for i, task in enumerate(tasks, start=1):
                                        print(f"{i}. {task.strip()}")
                        else:
                                print("No tasks found.")
        except FileNotFoundError:
                print("No tasks found")


def add_task(task):
        with open("tasks.txt", "a") as file:
                file.write(task + "\n")
        print("Task added successfully.")


def delete_task(task_number):
        try:
                with open("tasks.txt", "r") as file:
                        tasks = file.readlines()
                with open("tasks.txt", "w") as file:
                        if  1<= task_number <= len(tasks):
                                del tasks[task_number -1]
                                file.writelines(tasks)
                                print("Task deleted successfully")
                        else:
                                print("Invalid task number.")
        except FileNotFoundError:
                print("No task found")


while True:
        print("\n1. Show Tasks \n2. Add task \n3. Delete task \n4. Quit")
        choice = input("Enter Your Choice (1/2/3/4): ")

        if choice == "1":
                show_tasks()
        elif choice == "2":
                new_task = input("Enter the task: ")
                add_task(new_task)
        elif choice == "3":
                show_tasks()
                task_to_delete = int(input("Enter the task number to delete: "))
                delete_task(task_to_delete)
        elif choice == "4":
                print("Thanks for using this software, see you soon!")
                break
        else:
                print("Invalid choice. Please enter a valid option.")