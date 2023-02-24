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

"""
Dynamic programming

Here's how the code works:

Get the length of the input string s and create a 2D array dp of size (n, n) to store the result of subproblems. 
- We also initialize the max_len variable to 0 to keep track of the length of the longest palindrome found.

Fill in the base cases for substrings of length 1 and 2. 
- For substrings of length 1, the answer is always 1 since any single character is a palindrome. 
- For substrings of length 2, we check if the two characters are the same and mark the corresponding entry in dp as 1 if they are. 
- We also update max_len to 2 if a palindrome of length 2 is found.

For substrings of length 3 or more, we use dynamic programming to fill in the remaining entries in dp. 
- For each substring of length k, we check if the first and last characters are the same 
    and if the substring between them is also a palindrome (as indicated by the dp array). 
- If these conditions are met, we mark the corresponding entry in dp as 1 and update max_len to k+1 if k+1 is greater than the current value of max_len.

After all substrings have been checked, we return max_len as the length of the longest palindrome found.
"""
