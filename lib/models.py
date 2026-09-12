# TODO: Define the Task class
# Each task should store a title and a completed status (default False)
# Add a complete() method that marks the task as completed and prints confirmation

class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True
        print(f"✅ Task '{self.title}' completed.")

# TODO: Define the User class
# Each user has a name and a list of tasks
# Add methods to add tasks and search tasks by title

class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"📌 Task '{task.title}' added to {self.name}.")

    def get_task_by_title(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None