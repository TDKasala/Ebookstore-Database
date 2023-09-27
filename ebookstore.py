import sqlite3

# Connecting  to the database
db = sqlite3.connect('ebookstore.db')
cursor = db.cursor()

# Check if the books table exists
cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table' AND name='books'")
result = cursor.fetchone()

if not result:
    # Create the books table
    cursor.execute(
        '''CREATE TABLE books (id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)''')

# Insert the initial books into the table
books = [(3001, "A tale of two cities", "Charles dickens", 30),
         (3002, "Harry Potter and the Philosopher's stone", "J.K Rowling", 40),
         (3003, "The lion, The witch and The wardrobe", "C.S Lewis", 25),
         (3004, "The Lord of the rings", "J.R.R Tolkien", 37),
         (3005, "Alice in wonderland", "Lewis Caroroll", 12)]

cursor.executemany("INSERT OR IGNORE INTO books VALUES (?,?,?,?)", books)


# Function to add a new book to the database
def add_book(id, Title, Author, Qty):
    cursor.execute("INSERT INTO books VALUES (?,?,?,?)",
                   (id, Title, Author, Qty))
    db.commit()

    print("Book added successfully")

# Function to update a book's information
def update_book(id, Title=None, Author=None, Qty=None):
    cursor.execute("SELECT * FROM books WHERE id = ?", (id,))
    book = cursor.fetchone()
    if not book:
        print("Book not found")
        return
    if Title:
        cursor.execute("UPDATE books SET Title = ? WHERE id = ?", (Title, id))
    if Author:
        cursor.execute(
            "UPDATE books SET Author = ? WHERE id = ?", (Author, id))
    if Qty is not None:
        cursor.execute("UPDATE books SET Qty = ? WHERE id = ?", (Qty, id))
    db.commit()
    print("Book updated successfully")

# Function to delete a book from the database
def delete_book(id):
    cursor.execute("SELECT * FROM books WHERE id = ?", (id,))
    book = cursor.fetchone()
    if not book:
        print("Book not found")
        return
    cursor.execute("DELETE FROM books WHERE id = ?", (id,))
    db.commit()
    print("Book deleted successfully")

# Function to search for a specific book
def search_book(id):
    try:
        id = int(id)
    except ValueError:
        print("Invalid id")
        return
    cursor.execute("SELECT * FROM books WHERE id = ?", (id,))
    book = cursor.fetchone()
    if book:
        print("id:", book[0])
        print("Title:", book[1])
        print("Author:", book[2])
        print("Qty:", book[3])
    else:
        print("Book not found")


# Menu function to handle user input
def menu():
    while True:
        print("\nWelcome to Ebookstore Database\n")
        choice = input('''Please enter a number between 0 and 4: 
1. Enter a new book
2. Update a book
3. Delete a book
4. Search for a book
0. Exit
\n''')

        if choice == "1":
            id = input("Enter id: ")
            Title = input("Enter title: ")
            Author = input("Enter author: ")
            Qty = input("Enter quantity: ")
            add_book(id, Title, Author, Qty)

        elif choice == "2":
            id = input("Enter id: ")
            Title = input("Enter title: ")
            Author = input("Enter author: ")
            Qty = input("Enter quantity: ")
            update_book(id, Title, Author, Qty)

        elif choice == "3":
            id = input("Enter id: ")
            delete_book(id)

        elif choice == "4":
            id = input("Enter id: ")
            search_book(id)

        elif choice == "0":
            break

        else:
            print("Invalid choice")


# Run the menu function
menu()

# Close the connection
db.close()
