
# Module Lab: Building a Python Command-Line Interface Tool

A modular, object-oriented **Task Manager CLI** built with Python's `argparse`.
Users can add tasks to a name and mark them complete, with clear terminal
feedback and helpful error messages.

## Learning Goals

- Build modular and user-friendly command-line applications using `argparse`.
- Apply object-oriented programming (OOP) to map real-world objects to CLI commands.
- Validate user input and provide helpful feedback.
- Structure CLI tools for maintainability and scalability.

## Introduction

This project implements a Python Command-Line Interface (CLI) tool that models
real-world behavior using OOP. It uses Python's built-in `argparse` module to
define commands and object-oriented classes to manage task-related actions.

The CLI tool allows users to:

- Add tasks to a user account via `add-task`
- Mark tasks as complete via `complete-task`
- Display feedback directly in the terminal

The domain logic (the `Task` and `User` classes) is kept separate from the CLI
logic so the code stays modular, testable, and easy to extend.

## Project Structure

```
python_CLI/
├── lib/
│   ├── __init__.py
│   ├── models.py      # Task and User classes (domain logic)
│   └── cli_tool.py    # argparse CLI (command routing)
├── testing/
│   ├── __init__.py
│   └── test_cli_tool.py
├── Pipfile
├── pytest.ini
└── README.md
```

## Setup Instructions

### Fork and Clone the Repository

1. Fork the repository to your GitHub account.
2. Clone the fork to your local machine:

```bash
git clone <your-fork-url>
cd python_CLI
```

### Install Python and Dependencies

Ensure Python 3.12 is installed:

```bash
python --version
```

Dependencies are managed with **Pipenv** (see `Pipfile`). The only dependency is
`pytest` for running the test suite:

```bash
pip install pipenv
pipenv install
pipenv shell
```

Alternatively, with a plain virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
pip install pytest
```

## Usage

Run the CLI as a module from the project root (`python_CLI/`) so the `lib`
package resolves correctly:

```bash
# Add a task for a user
python -m lib.cli_tool add-task Alice "Write unit tests"
# 📌 Task 'Write unit tests' added to Alice.

# Show available commands
python -m lib.cli_tool
```

> **Note on state:** Data is held in memory for the duration of a single
> invocation, so state does not persist between separate commands. Running
> `add-task` and then a separate `complete-task` will report the user as not
> found — this is expected. The complete-task flow is exercised within one
> shared script/session (see the test suite).

### Commands

| Command         | Arguments        | Description                          |
| --------------- | ---------------- | ------------------------------------ |
| `add-task`      | `user` `title`   | Adds a task to the named user.       |
| `complete-task` | `user` `title`   | Marks the user's task as complete.   |

Both commands print a confirmation on success and a helpful `❌` message when a
user or task cannot be found.

## Design

The application is split into two layers:

- **`Task`** — represents a single task (a `title` and a `completed` flag) and
  exposes a `complete()` method that updates the status and prints confirmation.
- **`User`** — groups tasks under a name and exposes `add_task()` and
  `get_task_by_title()`.
- **CLI controller** — an `argparse` parser with `subparsers` that routes each
  command to a dedicated handler function via `set_defaults(func=...)`.

### `lib/models.py`

```python
class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True
        print(f"✅ Task '{self.title}' completed.")


class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"📌 Task '{task.title}' added to {self.name}.")

    def get_task_by_title(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None
```

### `lib/cli_tool.py`

```python
import argparse

# Works both as a module ("python -m lib.cli_tool") and run directly.
try:
    from lib.models import Task, User
except ImportError:
    from models import Task, User

users = {}


def add_task(args):
    user = users.get(args.user)
    if user is None:
        user = User(args.user)
        users[args.user] = user
    user.add_task(Task(args.title))


def complete_task(args):
    user = users.get(args.user)
    if user is None:
        print("❌ User not found.")
        return
    task = user.get_task_by_title(args.title)
    if task is None:
        print("❌ Task not found.")
        return
    task.complete()
```

## Running the Tests

From the project root:

```bash
python -m pytest testing/ -v
```

Expected output:

```
testing/test_cli_tool.py::test_add_task PASSED
testing/test_cli_tool.py::test_complete_task_with_script PASSED
```

## Best Practices Applied

- `argparse` subparsers map each command to a dedicated handler function.
- Input paths validated with helpful `❌` error messages.
- CLI logic and OOP domain logic kept in separate modules.
- The `if __name__ == "__main__":` guard keeps the script importable and reusable.

## Conclusion

This project demonstrates how to:

✅ Build a structured, modular CLI tool in Python
✅ Map real-world entities using object-oriented design
✅ Create a terminal experience with helpful input/output
✅ Apply `argparse` and OOP to a real development workflow
