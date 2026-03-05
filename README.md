# Task Manager CLI

A Python command-line interface tool for managing tasks organized by user.

## Overview

Task Manager CLI is a simple yet powerful command-line tool that allows users to create tasks and mark them as complete. Tasks are organized under user accounts, making it easy to manage different task lists for different people.

## Features

- **Add Tasks**: Create new tasks under a user account
- **Complete Tasks**: Mark existing tasks as completed
- **User-based Organization**: Group tasks by user name
- **Terminal Feedback**: Clear visual feedback for all operations

## Requirements

- Python 3.7+
- No external dependencies (uses Python standard library)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd python-cli-tool-lab
```

2. Ensure Python 3.7+ is installed:
```bash
python --version
```

## Usage

### Add a Task

```bash
python lib/cli_tool.py add-task <username> "<task-title>"
```

Example:
```bash
python lib/cli_tool.py add-task Alice "Write documentation"
```

Output:
```
📌 Task 'Write documentation' added to Alice.
```

### Complete a Task

```bash
python lib/cli_tool.py complete-task <username> "<task-title>"
```

Example:
```bash
python lib/cli_tool.py complete-task Alice "Write documentation"
```

Output:
```
✅ Task 'Write documentation' completed.
```

### View Help

```bash
python lib/cli_tool.py --help
```

## Project Structure

```
python-cli-tool-lab/
├── lib/
│   ├── __init__.py
│   ├── models.py          # Task and User classes
│   └── cli_tool.py        # CLI entry point
├── testing/
│   ├── __init__.py
│   └── test_cli_tool.py   # Unit tests
├── README.md
├── LICENSE.md
├── CONTRIBUTING.md
├── Pipfile
└── pytest.ini
```

## Development

### Running Tests

```bash
pytest
```

## License

See [LICENSE.md](LICENSE.md) for details.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.
