storage = {}
id_index = 0

def add():
    global id_index
    name = input("Name: ")
    author = input("Author: ")
    page_amount = input("Page amount: ")
    genre = input("Genre: ")
    binding = input("Binding: ")
    id_index += 1
    storage[id_index] = {"Name:":name,"Author":author,"Page amount:":page_amount,"Genre":genre,"Binding":binding}
    print("New book added!\nBook id:", id_index)
    print("===================")

def delete():
    id_choice = input("Enter the book id: ")
    if id_choice in storage:
        del storage[id_choice]
        print("Book deleted.")
        print("===================")
    else:
        print("Wrong ID.")
        print("===================")
    
def edit():
    id_choice = input("Enter book id: ")
    if id_choice in storage:
        name = input("Name: ")
        author = input("Author: ")
        page_amount = input("Page amount: ")
        genre = input("Genre: ")
        binding = input("Binding: ")
        storage[id_choice] = {"Name:":name,"Author":author,"Page amount:":page_amount,"Genre":genre,"Binding":binding}
        print("Book edited.")
        print("===================")
    else:
        print("Wrong ID.")
        print("===================")

def find():
    id_choice = int(input("Enter book ID: "))
    if id_choice in storage:
        print(storage[id_choice])
        print("===================")
    else:
        print("Wrong ID.")
        print("===================")

while True:
    print("1.Add\n2.Delete\n3.Edit\n4.Find")
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
        case _:
            print("Wrong action!")
            print("===================")