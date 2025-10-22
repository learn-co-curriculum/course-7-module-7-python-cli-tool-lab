import argparse
from lib.models import Task, User

users = {}  # key: user name -> value: User instance

def add_task(args):
    """
    CLI handler: add a task to a user.
    """
    # create the user if they don't exist yet
    user = users.get(args.user)
    if user is None:
        user = User(args.user)
        users[args.user] = user

    # create a new task and add it
    task = Task(args.title)
    user.add_task(task)

def complete_task(args):
    """
    CLI handler: mark a user's task as complete.
    """
    user = users.get(args.user)
    if user is None:
        print("❌ User not found.")
        return

    task = user.get_task_by_title(args.title)
    if task is None:
        print("❌ Task not found.")
        return

    task.complete()

def build_parser():
    """
    Build and return the top-level argparse parser with subcommands.
    """
    parser = argparse.ArgumentParser(
        description="Task Manager CLI"
    )
    subparsers = parser.add_subparsers()

    # add-task command
    add_parser = subparsers.add_parser("add-task", help="Add a task for a user")
    add_parser.add_argument("user", help="User name")
    add_parser.add_argument("title", help="Task title (use quotes for multi-word)")
    add_parser.set_defaults(func=add_task)

    # complete-task command
    complete_parser = subparsers.add_parser("complete-task", help="Complete a user's task")
    complete_parser.add_argument("user", help="User name")
    complete_parser.add_argument("title", help="Task title")
    complete_parser.set_defaults(func=complete_task)

    return parser

def main():
    """
    CLI entry point. Parse args and dispatch to the selected command.
    """
    parser = build_parser()
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()