def print_rhombus(size, i=1):
    if i <= size:
        print(" " * (size - i) + "* " * i)
        print_rhombus(size, i + 1)
        print(" " * (size - i) + "* " * i)
        
size = int(input("Enter the size of the rhombus: "))
print_rhombus(size)