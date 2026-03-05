# lib/cli_tool.py

import argparse
from lib.models import Task, User   # note: from lib.models

# Global dictionary to store users and their tasks
users = {}


def add_task(args):
    # Get existing user or create one
    user = users.get(args.user) or User(args.user)
    users[args.user] = user

    # Create the task
    task = Task(args.title)

    # Add the task (this prints the expected message)
    user.add_task(task)


def complete_task(args):
    user = users.get(args.user)
    if not user:
        print("❌ User not found.")
        return

    task = user.get_task_by_title(args.title)
    if not task:
        print("❌ Task not found.")
        return

    task.complete()


def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers()

    add_parser = subparsers.add_parser("add-task", help="Add a new task")
    add_parser.add_argument("user")
    add_parser.add_argument("title")
    add_parser.set_defaults(func=add_task)

    complete_parser = subparsers.add_parser(
        "complete-task", help="Complete a task"
    )
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
