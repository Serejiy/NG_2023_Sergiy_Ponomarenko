def draw_diamond(n):
    if n <= 0:
        return
    print("*" * n)
    draw_diamond(n - 1)
    print("*" * n)

n = int(input("Enter amount of stars: "))
draw_diamond(n)