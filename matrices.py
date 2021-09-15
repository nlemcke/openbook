def copy_matrix(matrix):
    """
    >>> copy_matrix([[1,2], [3,4]])
    [[1, 2], [3, 4]]
    >>> m = [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
    >>> copyofm = copy_matrix(m)
    >>> copyofm
    [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
    >>> for row_num, row in enumerate(copyofm):
    ...     for col_num, col_val in enumerate(row):
    ...         copyofm[row_num][col_num] = 42

    >>> copyofm
    [[42, 42, 42], [42, 42, 42], [42, 42, 42]]
    >>> m
    [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
    """
    new_matrix = []
    for row in matrix:
        new_matrix = new_matrix + [row[:]]
    return new_matrix



def add_row(matrix):
    """
      >>> m = [[0, 0], [0, 0]]
      >>> add_row(m)
      [[0, 0], [0, 0], [0, 0]]
      >>> n = [[3, 2, 5], [1, 4, 7]]
      >>> add_row(n)
      [[3, 2, 5], [1, 4, 7], [0, 0, 0]]
      >>> n
      [[3, 2, 5], [1, 4, 7]]
    """
    
    new_matrix = copy_matrix(matrix)
    new_row = []
    for value in matrix[0]:
        new_row.append(0)
    new_matrix.append(new_row)
    return new_matrix
        
def add_column(matrix):
    """
      >>> m = [[0, 0], [0, 0]]
      >>> add_column(m)
      [[0, 0, 0], [0, 0, 0]]
      >>> n = [[3, 2], [5, 1], [4, 7]]
      >>> add_column(n)
      [[3, 2, 0], [5, 1, 0], [4, 7, 0]]
      >>> n
      [[3, 2], [5, 1], [4, 7]]
    """

    new_matrix = copy_matrix(matrix)
    for row in new_matrix:
        row.append(0)
    return new_matrix

def transpose(m):
    """
     >>> m = [[3, 4, 6]]
     >>> transpose(m)
     [[3], [4], [6]]
     >>> m
     [[3, 4, 6]]
     >>> m = [[3, 4, 6], [1, 5, 9]]
     >>> transpose(m)
     [[3, 1], [4, 5], [6, 9]]
    """

    new_matrix = []
    for idx, val in enumerate(m[0]):
       new_matrix.insert(idx, [val])
    if len(m) > 1:
        for row in m[1:]:
            for idx, val in enumerate(row):
                new_matrix[idx].append(val)
    return new_matrix


if __name__ == '__main__':
    import doctest
    doctest.testmod()
