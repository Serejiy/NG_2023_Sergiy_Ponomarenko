first = int(input("First digit: "))
second = int(input("Second digit: "))
action = int(input("Choose action\n1)sum\n2)substract\n3)multiply\n4)divide\nYour choice: "))
match action:
    case 1:
        print("Sum =",first+second)
    case 2:
        print("Distraction =", first-second)
    case 3:
        print("Multiplication =",first*second)
    case 4:
        print("Division =",first/second)
    case _:
        print("Wrong action!")