import json
from datetime import date

# Main menu options
options = {
    1: "View outstanding tasks",
    2: "View all tasks",
    3: "Add task to list",
    4: "Mark task as done",
    5: "Remove task",
    9: "Exit"
}

today = date.today()

# Print list of tasks from JSON file.
# Parameter is a boolean that determines output mode. 
# False = print only uncompleted tasks, True = print all tasks.
# List is sorted by completion status then priority.
def print_tasks(print_all):
    with open('tasks.json', 'r+') as f:
        datastore = json.load(f)
        task_list = datastore['tasks']
        length = len(task_list)

        # key functions for sorting
        def sort_by_priority(list):
            return list['priority']
        def sort_by_done(list):
            return list['done']
            
        task_list.sort(key=sort_by_priority)
        task_list.sort(key=sort_by_done)

        print("   {: <20} {: <7} {: <10} {: <20} {: <20}".format('Task', 'Done?', 'Priority','Creation Date','Notes'))
        print("   -----------------------------------------------------------------------------------")
        #print(length, 'tasks in list')

        # iterate through and print sorted list
        count = 0
        for x,i in enumerate(task_list, start=1):            
            i['id'] = x
            if (print_all or not i.get('done')):
                print(" {: <2} {: <20} {: <7} {: <10} {: <20} {: <20}".format(x,i.get('name'),str(i.get('done')),i.get('priority'),i.get('creationdate'),i.get('notes')))
        f.truncate(0)
        f.seek(0)
        output = json.dumps(task_list)
        f.write(output)
        #json.dump(output, f, indent = 4)
    f.close()
    return task_list

def get_length():
    with open('tasks.json', 'r') as f:
        datastore = json.load(f)
        task_list = datastore['tasks']
        length = len(task_list)
    f.close()
    return length


# Append a task to the list
def add_task():
    name = input("Enter task name:")
    creationdate = today.strftime("%d/%m/%Y")
    priority = int(input("Enter priority level for task (1-3)"))
    notes = input("Enter notes (optional)")
    #print(name, " ", creationdate, " ", priority, " ", notes)
    

    # do something here to append this stuff to JSON file
    with open('tasks.json', 'r+') as f:
        datastore = json.load(f)
        new_data = {
        "id": get_length+1,
        "name": name,
        "creationdate": creationdate,
        "priority": priority,
        "done": False,
        "notes": notes
        }
        datastore["tasks"].append(new_data)
        f.seek(0)
        json.dump(datastore, f, indent = 4)
    f.close()

def complete_task():
    print("\nSelect a task to be marked as completed.\n")
    task_list = print_tasks(False)
    option = int(input("\nEnter a number:\n"))
    #print(task_list.pop(option-1).get('done'))
    
    with open('tasks.json', 'r+') as f:
        datastore = json.load(f)
        #print(datastore)
        new_data = {
            "id": get_length+1,
            "name": name,
            "creationdate": creationdate,
            "priority": priority,
            "done": False,
            "notes": notes
        }
        #json.dump(datastore, f, indent = 4)
    f.close()
    


def remove_task():
    print("remove_task() not yet implemented")

# Main menu driver function
def print_menu():
    print("\n\nEnter a number:\n")
    for i in options.keys():
        print(i,")", options[i])
    print()

while(True):
    print_menu()
    option = int(input("Enter a number: "))
    selection = options.get(option)
    if selection == "View outstanding tasks":
        print_tasks(False)
    elif selection == "View all tasks":
        print_tasks(True)
    elif selection == "Add task to list":
        add_task()
    elif selection == "Mark task as done":
        complete_task()
    elif selection == "Remove task":
        remove_task()
    elif option == 9:
        break
    else:
        print("Invalid selection. Please enter a number corresponding to one of the options on the list.")
    





