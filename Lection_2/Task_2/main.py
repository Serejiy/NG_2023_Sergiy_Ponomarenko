elements = input("Enter elements: ").split()
unique_elements = []
for element in elements:
    if elements.count(element) == 1:
        unique_elements.append(element)
print("Unique elements: ",unique_elements)