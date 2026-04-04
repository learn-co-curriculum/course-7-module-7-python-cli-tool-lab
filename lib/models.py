import json
import os

# Book class
class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def update_price(self, new_price):
        # Update the price of the book
        self.price = new_price
        print(f"Price of '{self.title}' updated to {self.price}")

    def restock(self, quantity):
        # Incrase the stock of the book by the given quantity
        self.stock += quantity
        print(f"Restocked '{self.title}'. New stock: {self.stock}")

    def sell(self):
        # Reduce the stock if available
        if self.stock > 0:
            self.stock -= 1
            print(f"Sold one copy of '{self.title}'. Remaining stock: {self.stock}")
        else:
            print(f"'{self.title}' is out of stock!")

    # Bookstore class(one and many relationship with books)
class Bookstore:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.load_from_file()

    def add_book(self, book):
        # Add a book to the bookstore's inventory
        self.books.append(book)
        self.save_to_file()
        print(f"Added '{book.title}' to {self.name} inventory.")

    def sell_book(self, title):
        # Sell a book by title
        book = self.get_book(title)
        if book:
            book.sell()
            self.save_to_file()

    def get_book(self, title):
        # Retrieve a book by title
        for book in self.books:
            if book.title == title:
                return book
            
        print(f"Book '{title}' not found in {self.name} inventory.")
        return None

    def list_books(self):
        # List all books in the bookstore
        if self.books:
            print(f"Books available in {self.name}:")
            for book in self.books:
                print(f"- {book.title} by {book.author} (${book.price}, Stock: {book.stock})")
        else:
            print(f"No books available in {self.name}.")

    def list_available(self):
        # List only available books (stock > 0)
        available_books = [book for book in self.books if book.stock > 0]
        if not available_books:
            print(f"No available books in {self.name}.")
            return
        print(f"Available books in {self.name}:")
        for book in available_books:
            print(f"- {book.title} by {book.author} (${book.price}, Stock: {book.stock})")

    def delete_book(self, title):
        # Remove a book from the inventory by title
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                self.save_to_file()
                print(f"Deleted '{title}' from {self.name} inventory.")
                return
        print(f"Book '{title}' not found in {self.name} inventory.")

    def save_to_file(self):
        
        os.makedirs("lib", exist_ok=True)  # Ensure the directory exists

        # Save the bookstore inventory to a JSON file
        data = [
            {
                "title": book.title, 
                 "author": book.author, 
                 "price": book.price, 
                 "stock": book.stock
                 }
                for book in self.books
            ]
        
        with open("lib/data.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self):
        # Load the bookstore inventory from a JSON file
        if os.path.exists("lib/data.json"):
            with open("lib/data.json", "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []

            self.books = [
                Book(item["title"], 
                     item["author"], 
                     item["price"], 
                     item["stock"])
                for item in data if isinstance(item, dict)
            ]
                               

    # Update stock
    def restock_book(self, title, quantity):
        # Restock a specific book by title
        book = self.get_book(title)
        if book:
            book.restock(quantity)
            self.save_to_file()


    # Update price
    def update_price(self, title, new_price):
        # Find book and update price
        book = self.get_book(title)
        if book:
            book.update_price(new_price)
            self.save_to_file()   
                                    
            