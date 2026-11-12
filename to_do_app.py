# add task 
# update task
# delete task
# find task
# view tasks
from datetime import datetime
from rich import print

class TaskManager:
    
    def __init__(self):
        self.memory = []

    def add_task(self, task: str):

        now = datetime.now()
        self.memory.append(
            {
                "Task":task,
                "Time": f"{now.hour}:{now.minute}"
            }
        )
        print("Task added successfully")

    def update_task(self, old_task: str, new_task: str):

        pass

    def view_tasks(self):

        num = 0
        for task in self.memory:
            print(f"Task {num+1} = ", task.get('Task'), f"({task.get('Time')})")
            num += 1

    def delete_task(self, task: str):
        pass

t = TaskManager()

while True:

    print("="*50)
    print(
        """
            1. Add Task
            2. Update Task
            3. Delete Task
            4. View Task
        """
    )
    user = int(input("Enter your choice (1/2/3/4) : "))

    if user == 1:
        task = input("Enter Task : ")
        t.add_task(task=task)

    elif user == 2:
        old_task = input("ENTER OLD TASK : ")
        new_task = input("ENTER NEW TASK : ")
        t.update_task(old_task=old_task, new_task=new_task)

    elif user == 3:
        task = input("ENTERTASK YOU WANT TO DELETE: ")
        t.delete_task(task=task)
        
    elif user == 4:
        if t.memory is not None:
            t.view_tasks()
        else:
            print("Enter task first")