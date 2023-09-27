# Ebookstore-Database

This is a simple Python script for managing a book inventory using SQLite. You can add, update, delete, and search for books in the database through a menu-driven command-line interface.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Functions](#functions)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- SQLite3 library for Python installed.

## Getting Started

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/ebookstore.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ebookstore
   ```

3. Run the `ebookstore.py` script to start the Ebookstore Database application.

## Usage

The Ebookstore Database application provides a menu-driven interface for managing books in the database. You can perform the following operations:

- **Add a new book**: Enter the book's ID, title, author, and quantity.

- **Update a book**: Enter the book's ID and update its title, author, or quantity.

- **Delete a book**: Enter the book's ID to remove it from the database.

- **Search for a book**: Enter the book's ID to view its details.

- **Exit**: Quit the application.

## Functions

### `add_book(id, Title, Author, Qty)`

Adds a new book to the database with the provided information.

### `update_book(id, Title=None, Author=None, Qty=None)`

Updates the information of an existing book in the database. You can specify which fields (Title, Author, Qty) to update.

### `delete_book(id)`

Deletes a book from the database based on its ID.

### `search_book(id)`

Searches for a specific book in the database based on its ID and displays its details.

### `menu()`

Displays the main menu and handles user input for various operations.

## Contributing

Contributions are welcome! If you have any improvements or suggestions for this project, please open an issue or a pull request.
