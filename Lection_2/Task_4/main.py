books = {}
id_counter = 0

def add_book():
    global id_counter
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the year of publication of the book: ")
    binding = input("Enter the binding type of the book: ")
    pages = input("Enter the amount of pages in the book: ")
    genre = input("Enter the genre of the book: ")
    id_counter += 1
    print ("The ID of your book is:",id_counter)
    books[id_counter] = {"Title": title, "Author": author, "Year": year, "Binding": binding, "Pages": pages, "Genre": genre}
    print("Book added!")
    print("====================")

def edit_book():
    book_id = int(input("Enter the ID of the book you want to edit: "))
    if book_id in books:
        title = input("Enter the new title of the book: ")
        author = input("Enter the new author of the book: ")
        year = input("Enter the new year of publication of the book: ")
        binding = input("Enter the new binding type of the book: ")
        pages = input("Enter the new amount of pages in the book: ")
        genre = input("Enter the new genre of the book: ")
        books[book_id] = {"Title": title, "Author": author, "Year": year, "Binding": binding, "Pages": pages, "Genre": genre}
        print("Book edited")
        print("====================")
    else:
        print("Book not found!")
        print("====================")

def delete_book():
    book_id = int(input("Enter the ID of the book you want to delete: "))
    if book_id in books:
        del books[book_id]
        print("Book deleted!")
        print("====================")
    else:
        print("Wrong book ID!")
        print("====================")

def view_book():
    book_id = int(input("Enter the ID of the book you want to view: "))
    if book_id in books:
        print("ID:", book_id)
        print("Title:", books[book_id]["Title"])
        print("Author:", books[book_id]["Author"])
        print("Year of publication:", books[book_id]["Year"])
        print("Binding type:", books[book_id]["Binding"])
        print("Number of pages:", books[book_id]["Pages"])
        print("Genre:", books[book_id]["Genre"],'\n')
    else:
        print("Wrong book ID")
        print("====================")

while True:
    print("1. Add a book")
    print("2. Edit a book")
    print("3. Delete a book")
    print("4. View a book")
    print("5. Exit")

    choice = input("Enter the number of the command you want to execute: ")

    if choice == 1:
        add_book()
    elif choice == 2:
        edit_book()
    elif choice == 3:
        delete_book()
    elif choice == 4:
        view_book()
    elif choice == 5:
        break
    else:
        print("Wrong action!")