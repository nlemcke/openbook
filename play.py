def seperate(list_of_stuff):
    empty = ([], [], [])
    for element in list_of_stuff:
        if type(element) == float or int:
            empty[0].append(element)
        if type(element) == str or list or tuple:
            empty[1].append(element)
        else:
            empty[2].append(element)
    return empty

print(seperate(['b']))
print(type('a'))
