empty = ([], [])
for element in [1, 2, 3, 4]:
    if element == 1 or element == 3:
        empty[0].append(element)
    elif element == 2 or 4:
        empty[1].append(element)
print(empty)
