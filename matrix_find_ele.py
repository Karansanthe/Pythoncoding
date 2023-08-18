def find(matrix, ele):
    for row in matrix:
        for item in row:
            if item == ele:
                return True
    return False

matrix = [[1, 2], [3, 4]]
ele = 7
print(find(matrix, ele))