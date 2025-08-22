import json
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

class Task:
    def __init__(self, title, due_date=None, priority='Normal'):
        self.title = title
        self.completed = False
        self.due_date = due_date
        self.priority = priority

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            'title': self.title,
            'completed': self.completed,
            'due_date': self.due_date,
            'priority': self.priority
        }

    @staticmethod
    def from_dict(data):
        task = Task(data['title'], data.get('due_date'), data.get('priority', 'Normal'))
        task.completed = data.get('completed', False)
        return task

class TodoList:
    def __init__(self):
        self.tasks = []  

    def add_tasks(self, title, due_date=None, priority='Normal'):  
        self.tasks.append(Task(title, due_date, priority)) 

    def edit_task(self,index,new_title=None, new_due_date=None, new_priority=None):
        if 0 <= index < len(self.tasks):
            tasks = self.tasks[index]

            if new_title:
                tasks.title = new_title
            if new_due_date is not None:
                tasks.due_date= new_due_date
            if new_priority:
                tasks.priority = new_priority

            else:
                print("No changes made to the task.")


    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()

    def save_to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f) 

    def load_from_json(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(item) for item in data]
        except FileNotFoundError:
            self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print(Fore.YELLOW + 'No tasks found.')
            return
        
        for i, task in enumerate(self.tasks):
            status = Fore.GREEN + '[✔]' if task.completed else Fore.RED + '[ ]'
            due_date = f" DUE: {task.due_date}" if task.due_date else ''
            priority = f" Priority: {task.priority}"
            print(f"{i+1}. {status} {task.title}{due_date}{priority}")


if __name__ == "__main__":
    todo = TodoList()
    
    