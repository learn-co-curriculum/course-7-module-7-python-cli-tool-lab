# cli_tool.py

import argparse
from .models import Task, User

# Global dictionary to store users and their tasks
users = {}

# Sample data for testing
alice = User("Alice")
unit_test_task = Task("Write unit tests")
alice.add_task(unit_test_task)
users["Alice"] = alice

def add_task(args):
    """Add a task for a user."""

    user = users.get(args.user)

    if user is None:
        user = User(args.user)
        users[args.user] = user
        print(f"👤 User '{args.user}' created.")

    try:
        task = Task(args.title)
        user.add_task(task)
    except ValueError as error:
        print(f"❌ {error}")


def complete_task(args):
     
    user = users.get(args.user)

    if user:
        user.complete_task(args.title)
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
