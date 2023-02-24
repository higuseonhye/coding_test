def solution(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    max_len = 0
    
    # base case for substrings of length 1
    for i in range(n):
        dp[i][i] = 1
        max_len = 1
    
    # base case for substrings of length 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 1
            max_len = 2
    
    # fill in remaining substrings of length 3 or more
    for k in range(2, n):
        for i in range(n-k):
            j = i + k
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = 1
                max_len = k+1
    
    return max_len
