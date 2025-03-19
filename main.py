# terminal to-do-task_list application
# 1. menu, the user can choose to access 1. main tasks, 2.subtasks, 3. all tasks
# 2. the user can add tasks and remove a task when done



# to continue: had a problem with the priority of the task when it gets created in All task page
# step taken:
# a class method created: set_priority(input)
# task_operator(list, priority=None) <-- set priority to optional in the task_operator function


import time
from task import Task


def display_task(task_list):
    if not task_list:
        print("\nCurrently no task")
    else:
        for i in task_list:
            print(i.toString())

def display_main_menu():
    print("\nWelcome to the menu!")
    print("1. Main task(s)")
    print("2. Sub-task(s)")
    print("3. All task(s)")
    print("4. Exit")
    print("\nTip: type \"help\" to display all commands")

def display_commands():
    print("\ntype \"add (task_name)\" to add a task")
    print("type \"remove (task_name)\" to remove a task")
    print("type \"done (task_name)\" to complete a task")
    print("type \"set (priority)\" to change the task's priority")
    print("type \"list\" to display the tasks list")
    print("type \"back\" to go back")
    print("type \"help\" to re-display all the commands")

def task_operator(task_list, priority=None):

    # loop until the user type "back"
    while True:
        task_command = input("\ncommand: ")

        # split the command into two parts: add task_name, remove task_name, done task_name.
        parts = task_command.split(" ", 1)

        if parts[0].lower() == "add" and len(parts) > 1:
            task_name = parts[1]
            task = Task(task_name, priority)
            task_list.append(task)
            print(f"\nThe task \"{task_name}\" has been created!")

        elif parts[0].lower() == "remove" and len(parts) > 1:

            task_to_remove = None
            for object_element in task_list:
                if object_element.name == parts[1]:
                    task_to_remove = object_element
                    break

            if task_to_remove is None:
                print("\nTask not found")
            else:
                task_list.remove(task_to_remove)
                print(f"\nThe task \"{task_to_remove.name}\" has been removed!")

        elif parts[0].lower() == "done" and len(parts) > 1:

            task_set_complete = None
            for object_element in task_list:
                if object_element.name == parts[1]:
                    task_set_complete = object_element
                    break
            if task_set_complete is None:
                print("\nTask not found")
            else:
                task_set_complete.task_completed()
                print(f"\nThe task {task_set_complete.name} has been set as completed!")
                print(task_set_complete.toString())

        elif task_command.lower() == "list":
            display_task(task_list)


        elif task_command.lower() == "help":
            display_commands()

        elif task_command.lower() == "back":
            display_main_menu()
            break

        else:
            print("\nInvalid Input\n")





## main program
main_task_list = []
sub_task_list = []
combined_list = main_task_list + sub_task_list

display_main_menu()

while True:
    mainNum = input("\ncommand: ")

    if mainNum == "1":
        print("\nMain-task List:")
        display_task(main_task_list)

        # if currently no task, display the commands
        if not main_task_list:
            display_commands()

        # expected the function here
        task_operator(main_task_list, "Main Task")



    elif mainNum == "2":
        print("\nSub-task List: ")
        display_task(sub_task_list)

        # if currently no task, display the commands
        if not sub_task_list:
            display_commands()


        task_operator(sub_task_list, "Sub-Task")

    elif mainNum == "3":
        print("\nAll-tasks List: ")
        display_task(combined_list)

        # if currently no task, display the commands
        if not combined_list:
            display_commands()

        task_operator(combined_list)

    elif mainNum == "4":

        # show that the program is ending
        print("\nTerminating the program\n"
              "Please wait...\n")
        time.sleep(2)
        break # exit the program


    elif mainNum.lower() == "help":

        # all commands in the main menu
        print("\ntype \"1\" to access Main tasks\n"
              "type \"2\" to access Sub-tasks\n"
              "type \"3\" to access All tasks\n"
              "type \"4\" to exit the program\n"
              "type \"menu\" to display the menu\n")


    elif mainNum.lower() == "menu":
        # re-displaying the main menu when type menu
        display_main_menu()


    else:
        # when user type invalid input
        print("\nInvalid Input!\n"
              "Please wait...\n")
        time.sleep(0.5)


print("Program stops!")