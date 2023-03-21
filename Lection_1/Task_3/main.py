first = int(input("First digit: "))
second = int(input("Second digit: "))
action = int(input("Choose action\n1)sum\n2)substract\n3)multiply\n4)divide\nYour choise: "))
if action == 1:
    print("Sum =",first+second)
elif action == 2:
    print("Distraction =", first-second)
elif action == 3:
    print("Multiplication =",first*second)
elif action == 4:
    print("Division =",first/second)
else:
    print("Wrong action!")