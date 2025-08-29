# todo.py

# Step 1: Start with an empty list to hold tasks
tasks = []

# Step 2: Add a task
def add_task(task):
    tasks.append(task)

# Step 3: View tasks
def view_tasks(tasks):
    List_Number = 1
    for item in tasks:
        print(str(List_Number) + " " + item)
        List_Number += 1


# Step 4: Delete a task

def delete_task(List):
    index = input("which task do you want deleted?")
    List.pop(int(index)-1)
    print("task deleted")


# Step 5: Mark task complete
def mark_complete(List):
    Completed = input("which task is complete?")
    Completed = int(Completed)
    List[Completed-1] = (List[Completed-1] + "/done")

# Step 6: Save/load tasks (extra stretch for today)
def save_tasks():
    pass


# Demo flow (you can run this file directly: python todo.py)
if __name__ == "__main__":
    add_task("Finish Cyber 201 assignment")
    add_task("Push code to GitHub")
    add_task("Victory Dance")
    view_tasks(tasks)

    delete_task(tasks)
    view_tasks(tasks)
    mark_complete(tasks)
    view_tasks(tasks)
    #save_tasks()

    # I don't completely understand what you mean by save tasks, so I'm gonna ignore it for now
