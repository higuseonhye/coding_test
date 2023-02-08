def dfs(numbers, target, idx, sum_val):
    if idx == len(numbers):
        if sum_val == target:
            return 1
        else:
            return 0
    return dfs(numbers, target, idx + 1, sum_val + numbers[idx]) + dfs(numbers, target, idx + 1, sum_val - numbers[idx])

def solution(numbers, target):
    return dfs(numbers, target, 0, 0)


"""
def dfs(numbers, target, i, sum, dp):
    if i == len(numbers):
        if sum == target:
            return 1
        else:
            return 0
    
    if dp[i][sum+1000] != -1:
        return dp[i][sum+1000]
    
    cnt = dfs(numbers, target, i+1, sum+numbers[i], dp) + dfs(numbers, target, i+1, sum-numbers[i], dp)
    dp[i][sum+1000] = cnt
    
    return cnt

def solution(numbers, target):
    dp = [[-1 for j in range(2001)] for i in range(20)]
    return dfs(numbers, target, 0, 0, dp)
"""
