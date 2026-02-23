import argparse
from models import Task, User

# Global dictionary to store users and their tasks
users = {}

# Function to add a task for a user
def add_task(args):
    username = args.user
    title = args.title

    # Check if the user exists, if not create one
    if username not in users:
        users[username] = User(username)
        print(f"User '{username}' created.")

    # Create a new Task
    task = Task(title)

    # Add task to the user
    users[username].add_task(task)


# Function to mark a task as complete
def complete_task(args):
    username = args.user
    title = args.title

    # Check if user exists
    if username not in users:
        print(f"Error: User '{username}' not found.")
        return

    user = users[username]

    # Look up the task
    task = user.get_task_by_title(title)

    if task is None:
        print(f"Error: Task '{title}' not found for user '{username}'.")
        return

    # Mark task as complete
    task.completed = True
    print(f"Task '{title}' marked as complete for {username}.")