import subprocess
import os

def run_cli_command(command):
    """Helper to run CLI command and capture output"""
    return subprocess.run(command, capture_output=True, text=True)

def test_add_task():
    result = run_cli_command(["python", "-m", "lib.cli_tool", "add-task", "Alice", "Submit report"])
    assert "📌 Task 'Submit report' added to Alice." in result.stdout

def test_complete_task_with_script(tmp_path):
    """Runs everything in one subprocess so state is shared."""
    script_path = tmp_path / "script.py"
    script_content = (
        "import sys, os\n"
        "sys.path.insert(0, '{0}')\n"
        "from lib.models import Task, User\n"
        "user = User('Bob')\n"
        "task = Task('Finish lab')\n"
        "user.add_task(task)\n"
        "task.complete()\n"
    ).format(os.getcwd().replace("\\", "/"))

    # write and run the script
    script_path.write_text(script_content)
    result = subprocess.run(["python", str(script_path)], capture_output=True, text=True)

    # check that the completion message appears
    assert "✅ Task 'Finish lab' completed." in result.stdout