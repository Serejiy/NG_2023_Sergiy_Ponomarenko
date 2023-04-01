storage = {}
id_index = 0

def template():
    name = input("Name: ")
    author = input("Author: ")
    page_amount = input("Page amount: ")
    genre = input("Genre: ")
    binding = input("Binding: ")
    return {"Name": name, "Author": author, "Page amount": page_amount, "Genre": genre, "Binding": binding}

def add():
    global id_index
    get_book_info = template()
    id_index += 1
    storage[id_index] = get_book_info
    print("New book added!\nBook id:", id_index)
    print("==============")
    
def edit():
    id_choice = int(input("Enter book id: "))
    if id_choice in storage:
        get_book_info = template()
        storage[id_choice] = get_book_info
        print("Book edited.")
        print("==============")
    else:
        print("Wrong ID.")
        print("==============")

def delete():
    id_choice = int(input("Enter the book id: "))
    if id_choice in storage:
        del storage[id_choice]
        print("Book deleted.")
        print("==============")
    else:
        print("Wrong ID.")
        print("==============")

def find():
    id_choice = int(input("Enter book ID: "))
    if id_choice in storage: 
        print(storage[id_choice])
        print("==============")
    else:
        print("Book not found!")
        print("==============")

while True:
    print("1.Add\n2.Delete\n3.Edit\n4.Find\n5.Exit")
    action = int(input("Choose action: "))

    match action:
        case 1:
            add()
        case 2:
            delete()
        case 3:
            edit()
        case 4:
            find()
        case 5:
            print("Goodbye!")
            exit()
        case default:
            print("Wrong action!")
