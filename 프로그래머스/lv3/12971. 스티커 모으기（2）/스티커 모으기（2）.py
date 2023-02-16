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

"""
The function solution takes a list of integers sticker as input and returns the maximum amount that can be obtained by selecting non-adjacent elements from sticker.

The code uses dynamic programming to solve the problem. It first checks for edge cases where the length of sticker is 1 or 2.

It then initializes two dynamic programming tables, dp1 and dp2, 
    which will store the maximum amount that can be obtained if we choose or don't choose the first sticker, respectively.

The code then iterates through sticker and fills in the values of dp1 and dp2 using the dynamic programming formula:
- dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i])
- where i is the current index, dp is either dp1 or dp2 depending on whether we are choosing the first sticker or not, and sticker is the input list.

Finally, the code returns the maximum amount that can be obtained by choosing or not choosing the first sticker, depending on which one yields the higher value.
"""
