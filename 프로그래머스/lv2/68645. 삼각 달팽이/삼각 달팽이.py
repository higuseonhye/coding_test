def solution(n):
    res = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0
    num = 1

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
               
            elif i % 3 == 2:
                x -= 1
                y -= 1
              
            res[x][y] = num
            num += 1
            
    for i in res:
        for j in i:
            if j != 0:
                answer.append(j)
    return answer

"""
The code solves the problem of generating a "snail array" from a given n. 
A snail array is a two-dimensional array that is filled in a spiral pattern.
Here is a step-by-step explanation of the code:

1. The res variable is a two-dimensional list of n lists, each with n elements, initialized to 0.
2. The answer variable is a list that will store the elements of the snail array in a one-dimensional format.
3. The variables x and y are the coordinates of the current element in the snail array. 
    - They are initialized to -1 and 0, respectively.
4. The num variable is a counter that will keep track of the current number to be placed in the snail array. 
    - It is initialized to 1.
5. The first for loop iterates n times, with i as the loop variable.
6. The second for loop iterates n times, with j as the loop variable.
7. Within the second for loop, an if-elif block is used to determine the direction to move next. 
    - If i % 3 is equal to 0, x is incremented by 1. If i % 3 is equal to 1, y is incremented by 1. 
    - If i % 3 is equal to 2, x and y are both decremented by 1.
8. The current number num is placed in the two-dimensional res list at the current coordinates x and y.
9. The num variable is then incremented by 1.
10. After the first two for loops, the elements in the two-dimensional res list are flattened into the one-dimensional answer list.
11. The function returns the answer list as the final result.

In summary, this code generates a snail array by iterating n times, 
    alternating between incrementing the x or y coordinate and decrementing both x and y coordinates, 
    and keeping track of the current number to be placed in the array. 
The final result is a one-dimensional list of the elements in the snail array.
"""
