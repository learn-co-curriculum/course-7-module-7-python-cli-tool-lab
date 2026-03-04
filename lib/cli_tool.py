# cli_tool.py
# lib/cli_tool.py
import argparse
import json
import os
import sys

# Global dictionary to store users and their tasks
users = {}
DB_FILE = "users.json"

# Import models correctly
try:
    from .models import Task, User
except ImportError:
    from models import Task, User

# Load users from file when program starts
def load_users():
    global users
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            data = json.load(f)
            users = {name: User.from_dict(user_data) for name, user_data in data.items()}
    else:
        users = {}

# Save users to file
def save_users():
    data = {name: user.to_dict() for name, user in users.items()}
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

# CLI functions
def add_task(args):
    user = users.get(args.user)
    if not user:
        user = User(args.user)
        users[args.user] = user
    
    task = Task(args.title)
    user.add_task(task)
    save_users()  # Save after adding

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
    save_users()  # Save after completing

def list_tasks(args):
    user = users.get(args.user)
    if not user:
        print("❌ User not found.")
        return
    
    if not user.tasks:
        print(f"{user.name} has no tasks.")
        return
    
    print(f"Tasks for {user.name}:")
    for i, task in enumerate(user.tasks, 1):
        status = "✅" if task.completed else "⏳"
        print(f"  {i}. {status} {task.title}")

# Main CLI parser
def main():
    load_users()  # Load at start
    
    parser = argparse.ArgumentParser(
        description="Task Manager CLI - Manage tasks for users",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli_tool.py add-task Alice "Write unit tests"
  python cli_tool.py complete-task Alice "Write unit tests"
  python cli_tool.py list-tasks Alice
        """
    )
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    add_parser = subparsers.add_parser("add-task", help="Add a task for a user")
    add_parser.add_argument("user", help="Username to add task for")
    add_parser.add_argument("title", help="Task title")
    add_parser.set_defaults(func=add_task)

    complete_parser = subparsers.add_parser("complete-task", help="Complete a user's task")
    complete_parser.add_argument("user", help="Username")
    complete_parser.add_argument("title", help="Task title to complete")
    complete_parser.set_defaults(func=complete_task)

    list_parser = subparsers.add_parser("list-tasks", help="List all tasks for a user")
    list_parser.add_argument("user", help="Username to list tasks for")
    list_parser.set_defaults(func=list_tasks)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()