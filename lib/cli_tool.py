import argparse
import os
import sys

# Support running directly or as a module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
try:
    from lib.models import Task, User
except ModuleNotFoundError:
    from models import Task, User

# Step 4: Seed users dictionary without triggering print output
users = {}
alice = User("Alice")
unit_test_task = Task("Write unit tests")
alice.tasks.append(unit_test_task)  # Direct append prevents extra print during setup
users["Alice"] = alice


def add_task(args):
    user = users.get(args.user)
    if not user:
        user = User(args.user)
        users[args.user] = user
    task = Task(args.title)
    user.add_task(task)


def complete_task(args):
    user = users.get(args.user)
    if user:
        task = user.get_task_by_title(args.title)
        if task:
            task.complete()
        else:
            print(f"Task '{args.title}' not found for user '{args.user}'.")
    else:
        print(f"User '{args.user}' not found.")


parser = argparse.ArgumentParser(description="Task Manager CLI")
subparsers = parser.add_subparsers()

# add-task command
add_parser = subparsers.add_parser("add-task", help="Add a new task")
add_parser.add_argument("user")
add_parser.add_argument("title")
add_parser.set_defaults(func=add_task)

# complete-task command
complete_parser = subparsers.add_parser("complete-task", help="Complete a task")
complete_parser.add_argument("user")
complete_parser.add_argument("title")
complete_parser.set_defaults(func=complete_task)

if __name__ == "__main__":
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()