matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for column in row:
        if column == row[1]:
            print(column, end=" ")
print()