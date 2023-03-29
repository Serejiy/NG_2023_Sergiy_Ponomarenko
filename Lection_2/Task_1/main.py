def count_elems():
    amount = int(input("Enter amount of elements: "))
    elements = []
    for number in range(amount):
        element = input(f"Enter element {number+1}: ")
        elements.append(element)
    count = input("Enter the name of element that should be counted: ")
    print("Amount of requested element: ", elements.count(count))
count_elems()