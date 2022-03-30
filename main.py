import json
from datetime import date

# Main menu options
options = {
    1: "View tasks",
    2: "Add task to list",
    3: "Mark task as done",
    4: "Remove task",
    9: "Exit"
}

today = date.today()

# Print list of tasks from JSON file, priority sorted by default
def print_tasks():
    with open('tasks.json', 'r') as f:
        datastore = json.load(f)
        def sort_by_priority(list):
            return list['priority']
        print("   {: <20} {: <7} {: <10} {: <20} {: <20}".format('Task', 'Done?', 'Priority','Creation Date','Notes'))
        print("   -----------------------------------------------------------------------------------")
        count = 0
        for i in sorted(datastore['tasks'], key=sort_by_priority):
            count += 1
            #print("- " + i['name'] + "                " + i['notes'])
            print(count, " {: <20} {: <7} {: <10} {: <20} {: <20}".format(i.get('name'),str(i.get('done')),i.get('priority'),i.get('creationdate'),i.get('notes')))
    f.close()

# Append a task to the list
def add_task():
    name = input("Enter task name:")
    creationdate = today.strftime("%d/%m/%Y")
    priority = int(input("Enter priority level for task (1-3)"))
    notes = input("Enter notes (optional)")
    #print(name, " ", creationdate, " ", priority, " ", notes)
    new_data = {
        "name": name,
        "creationdate": creationdate,
        "priority": priority,
        "done": False,
        "notes": notes
    }

    # do something here to append this stuff to JSON file
    with open('tasks.json', 'r+') as f:
        datastore = json.load(f)
        datastore["tasks"].append(new_data)
        f.seek(0)
        json.dump(datastore, f, indent = 4)
    f.close()

def complete_task():
    print("complete_task() not yet implemented")

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
    if selection == "View tasks":
        print_tasks()
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
    





