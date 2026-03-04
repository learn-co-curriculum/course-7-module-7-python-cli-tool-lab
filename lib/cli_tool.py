# cli_tool.py

import argparse
from lib.models import Task, User

# Global dictionary to store users and their tasks
users = {}

# TODO: Implement function to add a task for a user
def add_task(args):
    # - Check if the user exists, if not, create one
    # - Create a new Task with the given title
    # - Add the task to the user's task list
    user = users.get(args.user)
    if not user:
        user = User(args.user)
        users[args.user] = user
    task = Task(args.title)
    user.add_task(task)

# TODO: Implement function to mark a task as complete
def complete_task(args):
    # - Look up the user by name
    # - Look up the task by title
    # - Mark the task as complete
    # - Print appropriate error messages if not found
    user = users.get(args.user)
    if user:
        task = user.get_task_by_title(args.title)
        if task:
            task.complete()
        else:
            print("❌ Task not found.")
    else:
        print("❌ User not found.")

# CLI entry point
def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers()

    # Subparser for adding tasks
    add_parser = subparsers.add_parser("add-task", help="Add a task for a user")
    add_parser.add_argument("user")
    add_parser.add_argument("title")
    add_parser.set_defaults(func=add_task)

    # Subparser for completing tasks
    complete_parser = subparsers.add_parser("complete-task", help="Complete a user's task")
    complete_parser.add_argument("user")
    complete_parser.add_argument("title")
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
