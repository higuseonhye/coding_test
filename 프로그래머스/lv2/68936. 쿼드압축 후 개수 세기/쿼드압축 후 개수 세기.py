def solution(arr):
    # Initialize the length of the input array
    n = len(arr)
    # Initialize the count of zeros and ones to 0
    zero_count, one_count = 0, 0
    
    def compress(x, y, size):
        # Define the zero_count and one_count as non-local
        nonlocal zero_count, one_count
        # If the size of the sub-array is 1,
        if size == 1:
            # If the element of the sub-array is 0, increment the zero_count, 
            # otherwise, increment the one_count
            if arr[x][y] == 0:
                zero_count += 1
            else:
                one_count += 1
        # If the size of the sub-array is not 1,
        else:
            # Get the first element of the sub-array
            first = arr[x][y]
            # Initialize a flag indicating if all elements in the sub-array are the same as the first element
            flag = True
            # Check all elements in the sub-array
            for i in range(x, x + size):
                for j in range(y, y + size):
                    # If an element is not equal to the first element, set the flag to False
                    if arr[i][j] != first:
                        flag = False
                        break
                if not flag:
                    break
            # If all elements in the sub-array are the same,
            if flag:
                # If the first element is 0, increment the zero_count, 
                # otherwise, increment the one_count
                if first == 0:
                    zero_count += 1
                else:
                    one_count += 1
            # If all elements in the sub-array are not the same,
            else:
                # Divide the size of the sub-array by 2
                new_size = size // 2
                # Check the sub-arrays in the four quadrants
                for i in range(2):
                    for j in range(2):
                        # Compress each sub-array recursively
                        compress(x + i * new_size, y + j * new_size, new_size)
                    
    # Call the compress function with the input array and its length
    compress(0, 0, n)
    # Return the count of zeros and ones
    return [zero_count, one_count]

"""
This code is for a function named solution that takes an input arr, which is a two-dimensional list. 
The function returns a list of two integers, the number of occurrences of 0s and 1s in the input arr.

Here's how the code works:

1. First, the length of the input array is stored in the n variable.
2. Two variables, zero_count and one_count, are initialized to 0, these variables are used to store the number of 0s and 1s in the input array.
3, The compress function is defined inside the solution function. 
    - This function takes three inputs, x, y, and size, and updates the global zero_count and one_count variables.
4. If size is 1, the value at the index arr[x][y] is checked. 
    - If it's 0, zero_count is incremented by 1, and if it's 1, one_count is incremented by 1.
5. If size is not 1, the code checks if all the elements in the sub-array starting from (x, y) and of size size are the same. 
    - If they are, the code increments either zero_count or one_count based on the value of the elements in the sub-array.
6. If all the elements are not the same, the code calls the compress function four times with different arguments. 
    - Each call compresses a quarter of the sub-array into a smaller sub-array, and the process is repeated until the size of the sub-array becomes 1.
7. Finally, the solution function calls the compress function with (0, 0, n) as arguments and returns [zero_count, one_count].

This code implements the divide and conquer approach to solve the problem of counting the number of 0s and 1s in a two-dimensional binary array.
"""
