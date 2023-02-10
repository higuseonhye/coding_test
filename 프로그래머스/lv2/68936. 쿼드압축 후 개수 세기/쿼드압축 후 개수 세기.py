def solution(arr):
    n = len(arr)
    zero_count = 0
    one_count = 0
    
    def compress(x, y, size):
        nonlocal zero_count
        nonlocal one_count
        if size == 1:
            if arr[x][y] == 0:
                zero_count += 1
            else:
                one_count += 1
            return
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
