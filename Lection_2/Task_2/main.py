elements = input("Enter elements: ").split()
unique_elements = []
for a in elements:
    if elements.count(a) == 1:
        unique_elements.append(a)
print("Unique elements: ",unique_elements)