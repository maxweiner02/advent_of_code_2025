# Part One
with open('input.txt', 'r') as file:
    matrix = []
    result = 0
    for line_num, line in enumerate(file):
        stripped = line.rstrip('\n')
        matrix.append(list(stripped))

    def getTopLeft(matrix, row, col):
        if row == 0 or col == 0:
            return None
        return matrix[row - 1][col - 1]

    def getTop(matrix, row, col):
        if row == 0:
            return None 
        return matrix[row - 1][col]

    def getTopRight(matrix, row, col):
        if row == 0 or col == len(matrix[0]) - 1:
            return None
        return matrix[row - 1][col + 1]

    def getLeft(matrix, row, col):
        if col == 0:
            return None
        return matrix[row][col - 1]

    def getRight(matrix, row, col):
        if col == len(matrix[0]) - 1:
            return None
        return matrix[row][col + 1]

    def getBottomLeft(matrix, row, col):
        if row == len(matrix) - 1 or col == 0:
            return None
        return matrix[row + 1][col - 1]

    def getBottom(matrix, row, col):
        if row == len(matrix) - 1:
            return None
        return matrix[row + 1][col]

    def getBottomRight(matrix, row, col):
        if row == len(matrix) - 1 or col == len(matrix[0]) - 1:
            return None
        return matrix[row + 1][col + 1]

    neighbor_methods = [getTopLeft, getTop, getTopRight, getLeft, getRight, getBottomLeft, getBottom, getBottomRight]

    for row_num, row in enumerate(matrix):
        for col_num, item in enumerate(row):
            # if its a '.' we don't need to do anything
            if(item == '.'):
                continue
        
            count = 0
            # we can now assume that the item is an '@'
            for method in neighbor_methods:
                char = method(matrix, row_num, col_num)
                if char == '@':
                    count += 1
            if count < 4:
                result += 1

    print(result)

# Part Two
with open('input.txt', 'r') as file:
    matrix = []
    result = 0
    for line_num, line in enumerate(file):
        stripped = line.rstrip('\n')
        matrix.append(list(stripped))

    def getTopLeft(matrix, row, col):
        if row == 0 or col == 0:
            return None
        return matrix[row - 1][col - 1]

    def getTop(matrix, row, col):
        if row == 0:
            return None 
        return matrix[row - 1][col]

    def getTopRight(matrix, row, col):
        if row == 0 or col == len(matrix[0]) - 1:
            return None
        return matrix[row - 1][col + 1]

    def getLeft(matrix, row, col):
        if col == 0:
            return None
        return matrix[row][col - 1]

    def getRight(matrix, row, col):
        if col == len(matrix[0]) - 1:
            return None
        return matrix[row][col + 1]

    def getBottomLeft(matrix, row, col):
        if row == len(matrix) - 1 or col == 0:
            return None
        return matrix[row + 1][col - 1]

    def getBottom(matrix, row, col):
        if row == len(matrix) - 1:
            return None
        return matrix[row + 1][col]

    def getBottomRight(matrix, row, col):
        if row == len(matrix) - 1 or col == len(matrix[0]) - 1:
            return None
        return matrix[row + 1][col + 1]

    neighbor_methods = [getTopLeft, getTop, getTopRight, getLeft, getRight, getBottomLeft, getBottom, getBottomRight]

    while True:
        start_result = result
        for row_num, row in enumerate(matrix):
            for col_num, item in enumerate(row):
                # if its a '.' we don't need to do anything
                if(item == '.'):
                    continue
        
                count = 0
                # we can now assume that the item is an '@'
                for method in neighbor_methods:
                    char = method(matrix, row_num, col_num)
                    if char == '@':
                        count += 1
                if count < 4:
                    matrix[row_num][col_num] = '.'
                    result += 1
        if start_result == result:
            break


    print(result)
