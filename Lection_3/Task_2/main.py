def print_rhombus(size, i=1):
    if i <= size:
        num_spaces = abs(size - i)
        num_stars = i
        print(" " * num_spaces + "* " + "* " * (num_stars - 1))
        print_rhombus(size, i + 1)
        print(" " * num_spaces + "* " + "* " * (num_stars - 1))
    else:
        return

size = int(input("Enter the size of the rhombus: "))
print_rhombus(size)