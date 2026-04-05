# Bookstore CLI 

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [How to Use](#how-to-use)
- [Data Storage (JSON Structure)](#data-storage-json-structure)
- [Folder Structure](#folder-structure)
- [Future Improvements](#future-improvements)
- [Author](#author)


## Project Description
Bookstore CLI Tool is a Python-based Command Line Interface (CLI) application that allows users to manage a simple bookstore inventory.

The application demonstrates Object-Oriented Programming (OOP) concepts such as classes, objects, and file handling. It also uses JSON for data persistence, allowing books to be saved and loaded between sessions.

Users can add books, view available books, and search for specific books directly from the terminal.


## Features
- Add new books to the inventory
- View all available books
- View details of a specific book
- Persistent storage using JSON
- Automatic loading and saving of data
- Beginner-friendly CLI interface

---

## Technologies Used
- Python 3
- Object-Oriented Programming (OOP)
- JSON (for data storage)
- File Handling
- Command Line Interface (CLI)


## Setup Instructions

### 1. Clone the repository
1. git clone <your-repo-link>
2. Navigate to project folder 
cd python-cli-tool-lab
3. Run the application
python3 lib/cli_tool.py

## How to Use
1. Add a Book
python3 lib/cli_tool.py add-book "Python 101" "Guido" 300 5
2. View All Books
python3 lib/cli_tool.py list-books
3. View a Specific Book
python3 lib/cli_tool.py view-book "Python 101"

## Data Storage (JSON Structure)
The application stores data in:
- lib/data.json
- Expected Format:
JSON
{
  "name": "My Bookstore",
  "books": [
    {
      "title": "Python 101",
      "author": "Guido",
      "price": 300,
      "stock": 5
    }
  ]
}

## Folder Structure

python-cli-tool-lab/
├── lib/
│   ├── cli_tool.py
│   ├── models.py
│   ├── data.json
├── tests/
├── README.md
├── requirements.txt

## Future Improvements
1. Add book categories (Programming, Fiction, etc.)
2. Add update/edit book functionality
3. Add search by author
4. Improve CLI output formatting (tables, colors)
5. Add admin authentication system
6. Export data to CSV or PDF

## Author
Agnes Ng'anga
GitHub: https://github.com/Mwihaki112

