"""
models.py
---------
Domain classes for the CLI tool. Kept separate from CLI/argparse logic so
the "business rules" (what a Task/User/Product can do) don't depend on how
they're invoked (CLI, tests, another interface, etc.).
"""

from datetime import datetime


class Task:
    """A single to-do item belonging to a User."""

    def __init__(self, title: str, priority: str = "normal"):
        self.title = title
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now()

    def complete(self):
        if self.completed:
            print(f"⚠️  Task '{self.title}' was already completed.")
            return
        self.completed = True
        print(f"✅ Task '{self.title}' marked complete.")

    def __str__(self):
        status = "✔" if self.completed else "•"
        return f"[{status}] {self.title} (priority: {self.priority})"


class User:
    """A user who owns a list of tasks."""

    def __init__(self, name: str):
        self.name = name
        self.tasks: list[Task] = []

    def add_task(self, task: Task):
        self.tasks.append(task)
        print(f"📌 Task '{task.title}' added to {self.name}.")

    def find_task(self, title: str) -> Task | None:
        # Case-insensitive match so "Write Tests" and "write tests" both work.
        for task in self.tasks:
            if task.title.lower() == title.lower():
                return task
        return None

    def complete_task(self, title: str):
        task = self.find_task(title)
        if not task:
            print(f"❌ Task '{title}' not found for user '{self.name}'.")
            return
        task.complete()

    def list_tasks(self):
        if not self.tasks:
            print(f"📭 {self.name} has no tasks yet.")
            return
        print(f"🗒️  Tasks for {self.name}:")
        for task in self.tasks:
            print(f"   {task}")


class Product:
    """An inventory item that can be restocked or sold."""

    def __init__(self, name: str, quantity: int = 0, price: float = 0.0):
        self.name = name
        self.quantity = quantity
        self.price = price

    def restock(self, amount: int):
        self.quantity += amount
        print(f"📦 Restocked '{self.name}' by {amount}. New quantity: {self.quantity}.")

    def sell(self, amount: int):
        if amount > self.quantity:
            print(f"❌ Cannot sell {amount} of '{self.name}'; only {self.quantity} in stock.")
            return
        self.quantity -= amount
        print(f"🛒 Sold {amount} of '{self.name}'. Remaining: {self.quantity}.")

    def __str__(self):
        return f"{self.name}: qty={self.quantity}, price=${self.price:.2f}"


class TaskManager:
    """Keeps the in-memory registry of Users and routes task actions to them."""

    def __init__(self):
        self.users: dict[str, User] = {}

    def get_or_create_user(self, name: str) -> User:
        if name not in self.users:
            self.users[name] = User(name)
            print(f"👤 Created new user '{name}'.")
        return self.users[name]

    def get_user(self, name: str) -> User | None:
        return self.users.get(name)

    def list_users(self):
        if not self.users:
            print("📭 No users yet.")
            return
        print("👥 Users:")
        for user in self.users.values():
            done = sum(1 for t in user.tasks if t.completed)
            print(f"   {user.name}: {len(user.tasks)} task(s), {done} completed")


class Inventory:
    """Keeps the in-memory registry of Products."""

    def __init__(self):
        self.products: dict[str, Product] = {}

    def get_or_create_product(self, name: str, price: float = 0.0) -> Product:
        if name not in self.products:
            self.products[name] = Product(name, quantity=0, price=price)
            print(f"🆕 Created new product '{name}'.")
        return self.products[name]

    def get_product(self, name: str) -> Product | None:
        return self.products.get(name)

    def list_products(self):
        if not self.products:
            print("📭 No products yet.")
            return
        print("📦 Products:")
        for product in self.products.values():
            print(f"   {product}")