m = [[1, 2, 3], [4, 5, 6]]
new_matrix = []
for idx, val in enumerate(m[0]):
   new_matrix.insert(idx, [val])
if m[1]:
    for row in m[1:]:
        for idx, val in enumerate(row):
            new_matrix[idx].append(val)
print(new_matrix)
