lists = []
non_unique = []
lsts_amount = int(input("Enter the lists amount: "))


for list in range(lsts_amount):
    add = input(f"Enter the {list+1} list: ").split()
    lists.append(add)

for add in lists:
    for element in add:
        if add.count(element) > 1:
            non_unique.append(element)

print ("Non unique list : ", set(non_unique))