def todo_print(lis):
    count = 1
    for i in lis:
        print(str(count) + ". " + i)
        count += 1


finish = False

todo_manager = [
    "insert a new task",
    "remove a task",
    "show all the task",
    "close the program"
]
tasks = []

while not finish:
    todo_print(todo_manager)
    choice = int(input())
    if choice == 1:
        new_task = input("Tell me the new task: ")
        print("")
        tasks.append(new_task)
    elif choice == 2:
        print("These are your tasks")
        todo_print(tasks)
        print("")
        num_task = int(input("Which task you want to remove?"))
        print("")
        tasks.pop(num_task-1)
    elif choice == 3:
        print("These are your tasks")
        todo_print(tasks)
        print("")
    elif choice == 4:
        finish = True
    else:
        print("Wrong choice!")