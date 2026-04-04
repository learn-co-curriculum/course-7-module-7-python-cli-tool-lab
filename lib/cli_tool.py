# cli_tool.py

import argparse
from models import Book, Bookstore

store = Bookstore("My Bookstore")

def add_book(args):
    # Book object added to the store
    book = Book(args.title, args.author, args.price, args.stock)
    store.add_book(book)

def list_books(args):
    # List all books in the store
    store.list_books()

def view_books(args):
    # Get and display a single book
    book = store.get_book(args.title)
    if book:
        print(f"{book.title} by {book.author} (Ksh {book.price}, Stock: {book.stock})")

def update_price(args):
    # Update the price of a book
    store.update_price(args.title, args.price)

def restock_book(args):
    # Restock a book
    store.restock_book(args.title, args.quantity)

def sell_book(args):
    # Sell one copy of a book
    store.sell_book(args.title)

def delete_book(args):
    # Delete a book from the store
    store.delete_book(args.title)

def list_available(args):
    # List only available books
    store.list_available()



def main():
    parser = argparse.ArgumentParser(description="Bookstore CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add book command
    add_parser = subparsers.add_parser("add-book")
    add_parser.add_argument("title")
    add_parser.add_argument("author")
    add_parser.add_argument("price", type=float)
    add_parser.add_argument("stock", type=int)
    add_parser.set_defaults(func=add_book)

    # List books command
    list_cmd = subparsers.add_parser("list-books")
    list_cmd.set_defaults(func=list_books)

    # View book command
    view = subparsers.add_parser("view-book")
    view.add_argument("title")
    view.set_defaults(func=view_books)

    # update-price command
    price = subparsers.add_parser("update-price")
    price.add_argument("title")
    price.add_argument("price", type=float)
    price.set_defaults(func=update_price)

    # restock-book command
    restock = subparsers.add_parser("restock-book")
    restock.add_argument("title")
    restock.add_argument("quantity", type=int)
    restock.set_defaults(func=restock_book)

    # sell-book command

    sell = subparsers.add_parser("sell-book")
    sell.add_argument("title")
    sell.set_defaults(func=sell_book)

    # delete-book command
    delete = subparsers.add_parser("delete-book")
    delete.add_argument("title")
    delete.set_defaults(func=delete_book)

    # list-available command
    available = subparsers.add_parser("list-available")
    available.set_defaults(func=list_available)

    # execute command
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()        





