# TODO: Define the Task class
# Each task should store a title and a completed status (default False)
# Add a complete() method that marks the task as completed and prints confirmation

class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True
        print(f"✅ Task '{self.title}' completed.")  # ✅ emoji required by test

    def to_dict(self):
        """Convert Task to dictionary for JSON"""
        return {
            "title": self.title,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        """Create Task from dictionary"""
        task = cls(data["title"])
        task.completed = data["completed"]
        return task


class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"📌 Task '{task.title}' added to {self.name}.")  # 📌 emoji required by test

    def get_task_by_title(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def to_dict(self):
        """Convert User to dictionary for JSON"""
        return {
            "name": self.name,
            "tasks": [task.to_dict() for task in self.tasks]
        }

    @classmethod
    def from_dict(cls, data):
        """Create User from dictionary"""
        user = cls(data["name"])
        user.tasks = [Task.from_dict(task_data) for task_data in data["tasks"]]
        return user