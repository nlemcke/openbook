def recursive_max(nestedlist):
    
    largest = nestedlist[0]
    while type(largest) == type([]):
        largest = largest[0]

    for i in nestedlist:
        if type(i) == type([]):
            max_elem = recursive_max(i)

        else:
            largest = 
