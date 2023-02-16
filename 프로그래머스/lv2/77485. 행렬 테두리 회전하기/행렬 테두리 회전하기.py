def solution(rows, columns, queries):
    # Initialize the matrix with the given rows and columns
    matrix = [[j + i * columns for j in range(1, columns + 1)] for i in range(rows)]

    result = []
    
    # Perform the cyclic rotation for each query
    for query in queries:
        top, left, bottom, right = query
        
        temp = matrix[top - 1][left - 1]
        min_val = temp
        
        # Rotate top row
        for i in range(left, right):
            value = matrix[top - 1][i]
            matrix[top - 1][i] = temp
            temp = value
            min_val = min(min_val, temp)

        # Rotate right column
        for i in range(top, bottom):
            value = matrix[i][right - 1]
            matrix[i][right - 1] = temp
            temp = value
            min_val = min(min_val, temp)

        # Rotate bottom row
        for i in range(right - 2, left - 2, -1):
            value = matrix[bottom - 1][i]
            matrix[bottom - 1][i] = temp
            temp = value
            min_val = min(min_val, temp)

        # Rotate left column
        for i in range(bottom - 2, top - 2, -1):
            value = matrix[i][left - 1]
            matrix[i][left - 1] = temp
            temp = value
            min_val = min(min_val, temp)

        # Append the minimum value for the current query to the result
        result.append(min_val)

    return result
