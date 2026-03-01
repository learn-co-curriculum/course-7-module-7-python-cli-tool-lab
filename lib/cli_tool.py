# lib/cli_tool.py

import argparse
from lib.models import Task, User  # ✅ absolute import

# Global dictionary to store users and tasks
users = {}

def add_task(args):
    # Check if user exists
    if args.user not in users:
        users[args.user] = User(args.user)
    user = users[args.user]

    # Create task and add
    task = Task(args.title)
    user.add_task(task)

def complete_task(args):
    # Check user exists
    if args.user not in users:
        print(f"User '{args.user}' not found.")
        return
    user = users[args.user]

    # Find task
    task = user.get_task_by_title(args.title)
    if not task:
        print(f"Task '{args.title}' not found for {args.user}.")
        return

    # Complete task
    task.complete()

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers()

    # Add task
    add_parser = subparsers.add_parser("add-task", help="Add a task for a user")
    add_parser.add_argument("user")
    add_parser.add_argument("title")
    add_parser.set_defaults(func=add_task)

    # Complete task
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