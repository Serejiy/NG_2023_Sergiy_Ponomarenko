def count_elems():
    N = int(input("Enter amount of elements: "))
    elements = []
    for a in range(N):
        element = input(f"Enter element {a+1}: ")
        elements.append(element)
    count = input("Enter the name of element that should be counted: ")
    print("Amount of requested element: ",elements.count(count))
count_elems()