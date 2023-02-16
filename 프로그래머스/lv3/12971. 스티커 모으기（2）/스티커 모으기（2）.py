def solution(sticker):
    n = len(sticker)
    
    # Edge cases: check if the length of the sticker is 1 or 2
    if n == 1:
        return sticker[0]
    elif n == 2:
        return max(sticker[0], sticker[1])
    
    # Initialize dp table
    dp1 = [0] * n
    dp2 = [0] * n
    
    # Calculate the maximum amount we can get if we choose the first sticker
    dp1[0] = sticker[0]
    dp1[1] = dp1[0]
    for i in range(2, n - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])
        
    # Calculate the maximum amount we can get if we don't choose the first sticker
    dp2[1] = sticker[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])
    
    # Return the maximum amount we can get
    return max(dp1[n - 2], dp2[n - 1])
