import math

def add():
    print("Sum:",first_d+second_d)

def substract():
    print("Substraction: ",first_d-second_d)

def multiply():
    print("Multiplication: ",first_d*second_d)

def divide():
    print("Division: ",first_d/second_d)

def root():
    print("Root of the first digigt: ",math.sqrt(first_d))
    print("Root of the second digitL ",math.sqrt(second_d))

def power():
    print("Result: ",first_d**second_d)

while True:
    first_d = int(input("Enter the first digit: "))
    second_d = int(input("Enter the second digigt: "))
    action = int(input("1)Add\n2)Substract\n3)Multiply\n4)Divide\n5)Power\n6)Square root\nChoose operation: "))
    match action:
        case 1: add()
        case 2: substract()
        case 3: multiply()
        case 4: divide()
        case 5: power()
        case 6: root()
        case default: print("Wrong action!")