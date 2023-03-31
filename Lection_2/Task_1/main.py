def count_elems():
    elements = []
    amount = int(input("Enter amount of elements: "))
    for number in range(amount):
        number +=1
        element = input(f"{number}.Element: ")
        elements.append(element)
    count = input("Enter the name of element that should be counted: ")
    print("Amount of requested element: ", elements.count(count))
count_elems()