class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.title}' added for {self.name}.")

    def get_task_by_title(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def list_tasks(self):
        if not self.tasks:
            print(f"No tasks found for {self.name}.")
            return

        print(f"\nTasks for {self.name}:")
        for task in self.tasks:
            status = "✓" if task.completed else "✗"
            print(f"- {task.title} [{status}] : {task.description}")


class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False