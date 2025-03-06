def main():
    #intialize an empty list to store tasks
    tasks = []

    print("To-do List")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

    while True:
        #prompt user for input to choose an option
        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            #asks user how many tasks they want to add
            n_tasks = int(input("How many tasks do you want to add? "))

            for i in range(n_tasks):
                #get the task description from the user
                task = input("Enter the task: ")
                #append a dictionary with task and its status to task listt
                tasks.append({"task": task, "done": False})
                print("Task added!")

        elif choice == '2':
            #dislay all the tasks with their status
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            #ask user the task that should be marked as done
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                #set task status to done
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif choice == '4':
            #exit
            print("Exiting.")
            break
        else:
            #invalid inputt
            print("Invalid choice. Select a valid option.")

if __name__ == "__main__":
    main()