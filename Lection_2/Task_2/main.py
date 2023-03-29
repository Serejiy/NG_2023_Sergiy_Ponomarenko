elements = input("Enter elements: ").split()
unique_elements = []
for index in elements:
    if elements.count(index) == 1:
        unique_elements.append(index)
print("Unique elements: ",unique_elements)