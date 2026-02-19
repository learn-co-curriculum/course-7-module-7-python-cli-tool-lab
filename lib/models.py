# TODO: Define the Task class
# Each task should store a title and a completed status (default False)
# Add a complete() method that marks the task as completed and prints confirmation

class Task:
    def __init__(self, title):
        # TODO: Assign the title
        self.title = title
        # TODO: Set completed to False
        self.completed = False
        pass

    def complete(self):
        # TODO: Mark the task as complete
        self.completed = True
        # TODO: Print a confirmation message
        print(f"Task '{self.title}' marked as complete.")
        pass

# TODO: Define the User class
# Each user has a name and a list of tasks
# Add methods to add tasks and search tasks by title

class User:
    def __init__(self, name):
        # TODO: Store the user's name
        self.name = name
        # TODO: Initialize an empty list of tasks
        self.task=[]
        pass

    def add_task(self, task):
        # TODO: Add the task to the user's task list
        self.task.append(task)
        # TODO: Print a message confirming the task was added
        print(f"📌 Task '{task.title}' added to user '{self.name}'.")
    def get_task_by_title(self, title):
        # TODO: Search for a task by its title in the user's task list
        for t in self.task:
            if t.title == title:
                return t
        # TODO: Return the matching task or None
        return None