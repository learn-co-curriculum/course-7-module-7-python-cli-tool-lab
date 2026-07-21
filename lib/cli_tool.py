"""
cli_tool.py
-----------
Modular CLI for managing Users/Tasks and Products/Inventory.

Design notes:
- All "business logic" lives in models.py (Task, User, Product, TaskManager,
  Inventory). This file only wires user input to those objects.
- State (users, products) lives only in memory for the life of the process,
  as required. Because a brand-new process would lose that state after every
  single command, running the script with NO arguments drops you into an
  interactive session so you can issue many commands against the same
  in-memory state (see run_interactive_session). Running it WITH arguments
  executes a single one-shot command, which is handy for scripting/testing.
"""

import argparse
import shlex
import sys

from models import TaskManager, Inventory

# ---------------------------------------------------------------------------
# In-memory stores (module-level so every command in a session shares them)
# ---------------------------------------------------------------------------
task_manager = TaskManager()
inventory = Inventory()


# ---------------------------------------------------------------------------
# Input validators (used as `type=` callbacks so argparse rejects bad input
# before a handler function ever runs)
# ---------------------------------------------------------------------------
def positive_int(value: str) -> int:
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{value}' is not a valid integer.")
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"Quantity must be a positive integer, got {ivalue}.")
    return ivalue


def non_negative_float(value: str) -> float:
    try:
        fvalue = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{value}' is not a valid number.")
    if fvalue < 0:
        raise argparse.ArgumentTypeError(f"Price cannot be negative, got {fvalue}.")
    return fvalue


def non_empty_str(value: str) -> str:
    stripped = value.strip()
    if not stripped:
        raise argparse.ArgumentTypeError("Value cannot be empty.")
    return stripped


# ---------------------------------------------------------------------------
# Command handlers — each maps directly onto a class method
# ---------------------------------------------------------------------------
def add_task(args):
    user = task_manager.get_or_create_user(args.user)
    task = user.find_task(args.title)
    if task:
        print(f"'{args.title}' already exists for {args.user}; not adding a duplicate.")
        return
    from models import Task
    user.add_task(Task(args.title, priority=args.priority))


def complete_task(args):
    user = task_manager.get_user(args.user)
    if not user:
        print(f"User '{args.user}' not found.")
        return
    user.complete_task(args.title)


def list_tasks(args):
    user = task_manager.get_user(args.user)
    if not user:
        print(f"User '{args.user}' not found.")
        return
    user.list_tasks()


def list_users(args):
    task_manager.list_users()


def add_product(args):
    product = inventory.get_or_create_product(args.name, price=args.price)
    if args.quantity:
        product.restock(args.quantity)


def restock_product(args):
    product = inventory.get_product(args.name)
    if not product:
        print(f"Product '{args.name}' not found. Use 'add-product' first.")
        return
    product.restock(args.amount)


def sell_product(args):
    product = inventory.get_product(args.name)
    if not product:
        print(f"Product '{args.name}' not found.")
        return
    product.sell(args.amount)


def list_products(args):
    inventory.list_products()


# argparse wiring

class FriendlyArgumentParser(argparse.ArgumentParser):
    """Raises instead of calling sys.exit(), so a REPL session can recover
    from a bad command without killing the whole program."""

    def error(self, message):
        raise ValueError(message)


def build_parser() -> argparse.ArgumentParser:
    parser = FriendlyArgumentParser(
        prog="cli_tool",
        description="Manage users/tasks and products/inventory from the command line.",
    )
    subparsers = parser.add_subparsers(dest="command", metavar="<command>")

    # --- Task commands ---
    p = subparsers.add_parser("add-task", help="Add a task for a user (creates the user if needed)")
    p.add_argument("user", type=non_empty_str, help="User name")
    p.add_argument("title", type=non_empty_str, help="Task title")
    p.add_argument("--priority", choices=["low", "normal", "high"], default="normal",
                   help="Task priority (default: normal)")
    p.set_defaults(func=add_task)

    p = subparsers.add_parser("complete-task", help="Mark a user's task as complete")
    p.add_argument("user", type=non_empty_str)
    p.add_argument("title", type=non_empty_str)
    p.set_defaults(func=complete_task)

    p = subparsers.add_parser("list-tasks", help="List all tasks for a user")
    p.add_argument("user", type=non_empty_str)
    p.set_defaults(func=list_tasks)

    p = subparsers.add_parser("list-users", help="List all users and their task counts")
    p.set_defaults(func=list_users)

    # --- Product commands ---
    p = subparsers.add_parser("add-product", help="Add a new product to inventory")
    p.add_argument("name", type=non_empty_str)
    p.add_argument("--price", type=non_negative_float, default=0.0, help="Unit price (default: 0.0)")
    p.add_argument("--quantity", type=positive_int, default=0, help="Starting quantity (optional)")
    p.set_defaults(func=add_product)

    p = subparsers.add_parser("restock-product", help="Add stock to an existing product")
    p.add_argument("name", type=non_empty_str)
    p.add_argument("amount", type=positive_int, help="Units to add")
    p.set_defaults(func=restock_product)

    p = subparsers.add_parser("sell-product", help="Remove stock from an existing product")
    p.add_argument("name", type=non_empty_str)
    p.add_argument("amount", type=positive_int, help="Units to remove")
    p.set_defaults(func=sell_product)

    p = subparsers.add_parser("list-products", help="List all products in inventory")
    p.set_defaults(func=list_products)

    return parser


def dispatch(parser: argparse.ArgumentParser, argv: list[str]) -> None:
    """Parse argv with the given parser and run the matching handler."""
    args = parser.parse_args(argv)
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


# ---------------------------------------------------------------------------
# Interactive session (keeps in-memory data alive across many commands)
# ---------------------------------------------------------------------------
def run_interactive_session():
    parser = build_parser()
    print("=== Task & Inventory CLI ===")
    print("Type a command (e.g. 'add-task Alice \"Write tests\"'), 'help', or 'exit'.\n")

    while True:
        try:
            line = input("cli> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break

        if not line:
            continue
        if line in ("exit", "quit"):
            print("Goodbye.")
            break
        if line == "help":
            parser.print_help()
            continue

        try:
            dispatch(parser, shlex.split(line))
        except ValueError as e:
            # Raised by FriendlyArgumentParser.error() on bad input/args
            print(f"Error: {e}")
        except SystemExit:
            # argparse's -h/--help calls sys.exit(0); swallow it in the REPL
            pass


def main():
    argv = sys.argv[1:]
    if argv:
        # One-shot mode: run a single command and exit (state is not
        # persisted between separate process invocations).
        parser = build_parser()
        try:
            dispatch(parser, argv)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)
    else:
        # No arguments: start an interactive session so multiple commands
        # can share the same in-memory data.
        run_interactive_session()


if __name__ == "__main__":
    main()
