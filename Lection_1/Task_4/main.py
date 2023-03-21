a = float(input("Enter a value: "))
b = float(input("Enter b value: "))
c = float(input("Enter c value: "))
Discriminant = b*2 - 4*a*c
if Discriminant == 0:
    x = -b / (2 * a)
    print('x = ',x)
elif a == 0:
    print ("a value can not be a 0, try again")
    exit()
else:
    x1 = (-b + Discriminant ** 0.5) / (2 * a)
    x2 = (-b - Discriminant ** 0.5) / (2 * a)
    print("x1 = ",x1)
    print("x2 = ",x2)


