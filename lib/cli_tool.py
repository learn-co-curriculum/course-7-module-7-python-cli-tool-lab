# cli_tool.py

import argparse
from models import Task, User

# Global dictionary to store users
users = {}

alice = User("Alice")
unit_test_task = Task("Write unit tests")
alice.add_task(unit_test_task)

users["Alice"] = alice

def add_task(args):
    # Check if the user exists
    user = users.get(args.user)

    # If not, create a new user
    if not user:
        user = User(args.user)
        users[args.user] = user

    # Create a new task
    task = Task(args.title)

    # Add task to user
    user.add_task(task)


def complete_task(args):
    # Find the user
    user = users.get(args.user)

    if not user:
        print("❌ User not found.")
        return

    # Find the task
    task = user.get_task_by_title(args.title)

    if not task:
        print("❌ Task not found.")
        return

    # Complete the task
    task.complete()


def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")

    subparsers = parser.add_subparsers()

    # add-task command
    add_parser = subparsers.add_parser("add-task", help="Add a task for a user")
    add_parser.add_argument("user")
    add_parser.add_argument("title")
    add_parser.set_defaults(func=add_task)

    # complete-task command
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