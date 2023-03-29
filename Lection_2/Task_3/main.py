set1 = input("Enter elements of the first set: ").split()
set2 = input("Enter elements of the second set: ").split()
set3 = input("Enter elements of the third set: ").split()
unique_list = []
for element in set1:
    if set1.count(element)>1:
        unique_list.append(element)
for element in set2:
    if set2.count (element)>1:
        unique_list.append(element)
for element in set3:
    if set3.count (element)>1:
        unique_list.append(element)

print ("The set of non-unique elements:",set(unique_list))
