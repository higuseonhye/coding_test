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

"""
이 코드는 2차원 행렬(m x n)에서 지정된 구역(puddles)을 제외하고 (1,1)에서 (m,n)으로 가는 경로의 수를 구하는 프로그램입니다.

- route 2차원 리스트를 (n+1)x(m+1) 크기로 생성합니다.
- route[1][1]에 1을 할당하여, 시작점에서 경로가 시작되었음을 표시합니다.
- s가 3부터 m+n까지 반복하는 반복문을 수행합니다.
- x는 1부터 s 까지, y는 s-x로 계산됩니다.
- x가 m 이하이고 y가 n 이하일 때에만,
    만약 [x,y]가 puddles에 존재하지 않으면, route[y][x]는 route[y-1][x]+route[y][x-1]로 계산됩니다.
- route[n-1][m]+route[n][m-1]을 리턴하고, 1000000007으로 나눈 나머지 값을 리턴합니다.
"""
