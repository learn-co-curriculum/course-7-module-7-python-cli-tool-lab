#  Task Manager CLI

A simple **Command-Line Interface (CLI)** application built with Python that allows users to manage tasks using object-oriented programming (OOP) and `argparse`.

The tool supports adding tasks, listing tasks, and marking tasks as complete directly from the terminal.

---

##  Features

-  Create and manage users in-memory
-  Add tasks for a user
-  List all tasks for a user
-  Mark tasks as completed
-  Lightweight CLI using `argparse`
-  Object-Oriented Design (Task + User classes)

---

##  Project Structure


lib/
│
├── cli_tool.py     # CLI entry point
├── models.py       # Task and User classes
└── __init__.py

## Installation

Clone the repository:

git clone git@github.com:wanja-juma/course-7-module-7-python-cli-tool-lab.git

cd task-manager-cli

## How It Works

Each User holds a list of Task objects.
Each Task has:
- title
- completed status
CLI commands map directly to Python functions using argparse.
Data is stored in memory only (no database or file storage).

### Testing

Run tests using:

pytest

### Future Improvements

Persistent storage (JSON or database)
Delete tasks functionality
Due dates and priorities
User authentication
Export tasks to file

### Tech Stack

Python 3
argparse (CLI handling)
OOP (classes and objects)
pytest (testing)