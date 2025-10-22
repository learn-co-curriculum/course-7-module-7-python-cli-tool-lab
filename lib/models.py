class Task:
    def __init__(self, title: str):
        # store the title and mark as not completed yet
        self.title = title
        self.completed = False

    def complete(self):
        # mark the task as done and print a confirmation
        self.completed = True
        print(f"✅ Task '{self.title}' completed.")

class User:
    def __init__(self, name: str):
        # store the user's name and start with an empty task list
        self.name = name
        self.tasks = []

    def add_task(self, task: Task):
        # keep the task and print a friendly message
        self.tasks.append(task)
        print(f"📌 Task '{task.title}' added to {self.name}.")

    def get_task_by_title(self, title: str):
        # find a task with the given title or return None
        for t in self.tasks:
            if t.title == title:
                return t
        return None