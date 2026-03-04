# models.py

class Task:
    def __init__(self, title):
        # Assign the title
        self.title = title
        
        # Task starts incomplete
        self.completed = False

    def complete(self):
        # Mark the task as completed
        self.completed = True
        
        # Print confirmation
        print(f"✅ Task '{self.title}' completed.")


class User:
    def __init__(self, name):
        # Store user name
        self.name = name
        
        # Initialize empty list of tasks
        self.tasks = []

    def add_task(self, task):
        # Add task to user's task list
        self.tasks.append(task)
        
        # Confirmation message
        print(f"📌 Task '{task.title}' added to {self.name}.")

    def get_task_by_title(self, title):
        # Search through the tasks
        for task in self.tasks:
            if task.title == title:
                return task
        
        # Return None if not found
        return None