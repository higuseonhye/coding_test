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
DFS를 사용한 방법은 코드가 간단하고 이해하기 쉽지만, 많은 수의 타겟 넘버를 만드는 방법을 구할 때는 시간이 많이 걸릴 수 있습니다.
"""
"""
- 이 코드는 깊이 우선 탐색(DFS) 알고리즘을 사용하여 "numbers" 배열에서 정수의 합이 "target"과 같은 경우의 수를 찾는 것입니다.
- dfs 함수는 깊이 우선 탐색을 수행하기 위한 함수입니다. "numbers" 배열, "target" 값, 현재 탐색 위치 "idx", 현재 합 "sum_val"을 인자로 받습니다.
- 만약 "idx"가 "numbers" 배열의 크기와 같다면, 타겟과 현재 합 "sum_val"이 같으면 1을 반환하고, 그렇지 않으면 0을 반환합니다.
- 그렇지 않은 경우, "numbers" 배열에서 현재 "idx"에 해당하는 숫자를 더하거나 빼어 "dfs" 함수를 다시 호출하여 탐색을 수행합니다. 
    두 번의 탐색 결과를 합하여 반환합니다.
- solution 함수는 "numbers" 배열과 "target" 값을 인자로 받아 "dfs" 함수를 호출하여 결과 값을 반환합니다.
"""


"""
비트 연산을 사용한 방법은 빠르게 타겟 넘버를 만드는 방법을 구할 수 있지만, 코드가 어렵고 이해하기 어렵다는 단점이 있습니다.
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
dfs 함수:

if문을 통해 현재 숫자의 인덱스가 주어진 숫자 리스트의 길이와 같아지면, 현재까지의 합이 타겟 넘버와 같으면 1을 반환하고 그렇지 않으면 0을 반환합니다.
메모이제이션을 위해 현재의 상태(i, sum)에 대한 결과값이 저장되어 있으면 그 결과값을 반환합니다.
현재 숫자에 +1하거나 -1하여 더한 값으로 dfs 함수를 다시 호출하여 얻은 결과를 더하여 결과를 반환합니다.
현재의 상태(i, sum)에 대한 결과값을 메모이제이션 배열에 저장합니다.
solution 함수:

메모이제이션 배열을 초기화합니다.
dfs 함수를 호출하여 결과를 반환합니다.
"""
