# TODO: Define the Task class
# Each task should store a title and a completed status (default False)
# Add a complete() method that marks the task as completed and prints confirmation

class Task:
    def __init__(self, title):
        if not title.strip():
            raise ValueError("Task title cannot be empty.")

        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True
        print(f"✅ Task '{self.title}' completed.")

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title}"

class User:
    def __init__(self, name):
        if not name.strip():
            raise ValueError("User name cannot be empty.")

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

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.complete()
                return

        print("❌ Task not found.")