def solution(arr):
    n = len(arr)
    zero_count, one_count = 0, 0
    
    def compress(x, y, size):
        nonlocal zero_count, one_count
        if size == 1:
            if arr[x][y] == 0:
                zero_count += 1
            else:
                one_count += 1
        else:
            first = arr[x][y]
            flag = True
            for i in range(x, x + size):
                for j in range(y, y + size):
                    if arr[i][j] != first:
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                if first == 0:
                    zero_count += 1
                else:
                    one_count += 1
            else:
                new_size = size // 2
                for i in range(2):
                    for j in range(2):
                        compress(x + i * new_size, y + j * new_size, new_size)
                    
    compress(0, 0, n)
    return [zero_count, one_count]


"""
This solution uses a helper function compress to perform the compression recursively. - The compress function takes three parameters: the starting x and y coordinate of the area to be compressed and the size of the area. 
- If the area has a size of 1, the value in the area will be counted as either 0 or 1. 
- If the area has a size larger than 1, it will be divided into four equal parts and the compress function will be called recursively for each part. 
- The compress function uses a flag to check if the area can be compressed into one value, and if so, the value will be counted as either 0 or 1. 
- If the area cannot be compressed into one value, the area will be divided into four parts and the compress function will be called recursively for each part. 
- The final result is a list of two numbers representing the number of 0s and the number of 1s in the compressed array.
"""