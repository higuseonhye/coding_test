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


"""
The solution function takes three arguments: rows, columns, and queries. 
The rows and columns parameters represent the dimensions of the matrix, while the queries parameter is a list of queries that specify the submatrix to be rotated.

The function first initializes the matrix with the given dimensions. 
It then iterates through each query and performs the cyclic rotation on the submatrix defined by the query.

For each query, the function uses four loops to rotate the top row, right column, bottom row, and left column of the submatrix. 
The minimum value of the submatrix is also tracked during the rotation.

After all queries have been processed, the function returns a list of the minimum values for each query.
"""
