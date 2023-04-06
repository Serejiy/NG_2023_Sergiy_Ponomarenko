def draw_diamond(amount):
    if amount <= 0:
        return
    print("*" * amount)
    draw_diamond(amount - 1)
    print("*" * amount)

amount = int(input("Enter amount of stars: "))
draw_diamond(amount)