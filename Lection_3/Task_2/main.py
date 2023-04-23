size = int(input("Enter the size of the rhombus: "))

for i in range(size):
    print(" "*(size-i-1) + "* "*(i+1))

for i in range(size-1, 0, -1):
    print(" "*(size-i) + "* "*(i))