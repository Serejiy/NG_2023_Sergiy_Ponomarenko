set1 = input("Enter elements of the first set: ").split()
set2 = input("Enter elements of the second set: ").split()
set3 = input("Enter elements of the third set: ").split()
unique_list = []
for a in set1:
    if set1.count(a)>1:
        unique_list.append(a)
for a in set2:
    if set2.count (a)>1:
        unique_list.append(a)
for a in set3:       
    if set3.count (a)>1:
        unique_list.append(a)

print ("The set of non-unique elements:",set(unique_list))
