# models.py
# Data models for the Task Manager CLI.
# Keeping the domain logic (Task / User) separate from the CLI logic
# keeps the code modular, testable, and easy to extend.


class Task:
    """A single task with a title and a completion status."""

    def __init__(self, title):
        self.title = title
        self.completed = False

    def complete(self):
        """Mark the task as completed and print a confirmation."""
        self.completed = True
        print(f"✅ Task '{self.title}' completed.")


class User:
    """A user who owns a list of tasks."""

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        """Add a task to this user and confirm."""
        self.tasks.append(task)
        print(f"📌 Task '{task.title}' added to {self.name}.")

    def get_task_by_title(self, title):
        """Return the first task matching the title, or None."""
        for task in self.tasks:
            if task.title == title:
                return task
        return None
