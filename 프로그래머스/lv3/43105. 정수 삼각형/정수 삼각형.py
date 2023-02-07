def solution(triangle):
    n = len(triangle)
    dp = [0] * (n+1)
    for i in range(1, n+1):
        for j in range(i, 0, -1):
            dp[j] = max(dp[j-1], dp[j]) + triangle[i-1][j-1]
    return max(dp)

"""
The optimization made in the code is that it uses only one dimensional array dp instead of a two dimensional array dp as in the original code. 
This optimization reduces the memory usage and also makes the code more efficient. 
In the original code, dp[i][j] only depends on dp[i-1][j-1] and dp[i-1][j], so using a two dimensional array is not necessary. 
The optimized code uses a one dimensional array and updates the values in place by using a loop that iterates in reverse order. 
This results in a more memory-efficient and faster implementation.
"""
"""
이 코드는 값의 삼각형에서 최대 합 경로를 찾는 문제의 해답입니다. 
    삼각형은 내장 리스트의 정수로 표현되어 있으며, triangle에 저장되어 있습니다.

이 코드는 문제를 해결하기 위해 동적 프로그래밍의 접근법을 사용하며, 각 요소의 최대 합은 dp 리스트에 저장됩니다. 
    dp 리스트는 n + 1개의 0으로 시작합니다. 
    여기서 n은 삼각형의 행 수입니다.

코드에는 두 개의 중첩 루프가 있습니다. 외부 루프 for i in range(1, n + 1)은 삼각형의 행을 반복합니다. 
    내부 루프 for j in range(i, 0, -1)은 각 행의 요소를 오른쪽에서 왼쪽으로 반복합니다.

내부 루프에서, dp[j]의 값은 dp[j-1]과 dp[j]의 최댓값에서 triangle[i-1][j-1] 값을 더한 것으로 업데이트됩니다. 
    max 함수는 dp[j-1]과 dp[j] 중 최대값을 찾기 위해 사용
"""
"""
This code is a solution to the problem of finding the maximum sum path in a triangle of values. 
The triangle is represented as a nested list of integers in triangle.

The code uses a dynamic programming approach to solve the problem, with the maximum sum for each element in the triangle being stored in the dp list. 
The dp list starts with n + 1 zeros, where n is the number of rows in the triangle.

The code has two nested loops. The outer loop for i in range(1, n + 1) iterates over the rows of the triangle. 
The inner loop for j in range(i, 0, -1) iterates over the elements in each row, from right to left.

In the inner loop, the value of dp[j] is updated to be the maximum of dp[j-1] and dp[j], plus the value of the element in the triangle at triangle[i-1][j-1]. 
The max function is used to find the maximum of dp[j-1] and dp[j], 
    as only one of these two values can be taken as the previous step in the path to reach the current element.

Finally, the code returns the maximum value in the dp list, which represents the maximum sum path through the triangle.
"""



def solution(triangle):
    n = len(triangle)
    dp = [[0] * (i + 1) for i in range(n)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    return max(dp[n-1])
"""
이 코드는 삼각형 모양의 각 층을 표현한 리스트 triangle을 매개변수로 받아, 그 중 가장 큰 경로의 합을 반환하는 것이다.

먼저, dp 리스트를 생성하여 triangle의 크기에 맞게 초기화한다. 
그리고, 초기에 dp[0][0]에 triangle의 첫 번째 요소인 triangle[0][0]을 할당한다.

그 후, triangle의 각 층을 반복하며 dp 리스트를 계산한다. j 값이 0일 경우에는 dp[i][j]는 dp[i-1][j] + triangle[i][j]가 된다. 
j 값이 i 일 경우에는 dp[i][j]는 dp[i-1][j-1] + triangle[i][j]가 된다. 그 외에는 dp[i][j]는 dp[i-1][j-1]와 dp[i-1][j] 중 큰 값 + triangle[i][j]가 된다.

마지막으로 dp[n-1] 리스트에서 가장 큰 값을 반환하여 경로의 합을 나타낸다.
"""
