# TO DO APP
from datetime import datetime
import pandas as pd
from rich import print

class TaskManager:
    
    def __init__(self):
        self.memory = []

    def add_task(self, task: str, date: str, time: str):

        try:

            scheduled_time = pd.to_datetime(
                f"{date} {time}",
                format="%d-%m-%Y %I:%M %p"
            )

            if scheduled_time <= pd.Timestamp.now():
                print("Enter future date and time !")
                return

        except ValueError as v:
            print("Problem occurred in date or time.")
            return

        self.memory.append(
            {
                "Task":task,
                "Time": scheduled_time,
                "status":"pending"
            }
        )
        print("Task added successfully")

    def update_task(self, old_task: str, new_task: str, new_date: str, new_time: str):

        for tasks in self.memory:
            if tasks['Task'] == old_task:
                tasks['Task'] = new_task
                scheduled_time_2 = pd.to_datetime(
                                f"{new_date} {new_time}",
                                format="%d-%m-%Y %I:%M %p"
                )
                if scheduled_time_2 <= pd.Timestamp.now():
                    print("Enter future date and time !")
                    return
                tasks['Time'] = scheduled_time_2
                print("Task updated successfully !")
                return
            else:
                print("Task not found !")

    def view_tasks(self):

        print("Total task added : ",len(self.memory))
        num = 0
        for task in self.memory:
            print(
                f"Task {num+1} = ", 
                task.get('Task'), 
                f"({task.get('Time')})", 
                f"STATUS : {task.get('status')}"
            )
            num += 1

    def delete_task(self, tasks: str):

        for task in self.memory:
            if task['Task'] == tasks:
                self.memory.remove(task)
                print("Task deleted successfully.")
                return
            
        print("Task not found !")

    def modify_status(self):
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
        date = input("Enter date (DD-MM-YYYY): ")
        time = input("Enter time (HH:MM AM/PM): ")
        t.add_task(task=task, date=date, time=time)

    elif user == 2:
        old_task = input("ENTER OLD TASK : ")
        new_task = input("ENTER NEW TASK : ")
        new_dates = input("Enter date (DD-MM-YYYY): ")
        new_times = input("Enter time (HH:MM AM/PM): ")
        t.update_task(old_task=old_task, new_task=new_task, new_date=new_dates, new_time=new_times)

    elif user == 3:
        task = input("Enter task you want to delete : ")
        t.delete_task(tasks=task)
        
    elif user == 4:
        if t.memory is not None:
            t.view_tasks()
        else:
            print("Enter task first")