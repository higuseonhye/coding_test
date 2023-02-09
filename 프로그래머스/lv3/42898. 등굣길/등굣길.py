def solution(m, n, puddles):
    MOD = 1000000007
    route = [[0 for _ in range(m+1)] for _ in range(n+1)]
    route[1][1] = 1
    for s in range(3, m+n):
        for x in range(1, s):
            y = s-x
            if x <= m and y <= n:
                if [x,y] not in puddles:
                    route[y][x] = route[y-1][x]+route[y][x-1]
    return (route[n-1][m]+route[n][m-1])%MOD




