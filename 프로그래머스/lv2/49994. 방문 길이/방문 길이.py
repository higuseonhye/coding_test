def solution(dirs):
    x, y = 0, 0
    visit = set()
    answer = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for d in dirs:
        nx, ny = x + dx[['U', 'R', 'D', 'L'].index(d)], y + dy[['U', 'R', 'D', 'L'].index(d)]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if (x, y, nx, ny) not in visit and (nx, ny, x, y) not in visit:
                visit.add((x, y, nx, ny))
                answer += 1
            x, y = nx, ny
    return answer

"""
코드의 목적은 주어진 "dirs" 문자열을 기반으로 경로의 수를 계산하는 것입니다.

- x, y 변수를 0으로 설정합니다. 이 변수는 현재 위치를 기억하기 위한 것입니다.
- "visit" set을 생성합니다. 이 set은 이미 방문한 경로를 기억하기 위한 것입니다.
- "answer" 변수를 0으로 설정합니다. 이 변수는 경로의 수를 기억하기 위한 것입니다.
- "dx"와 "dy" 리스트를 생성합니다. 이 리스트는 각 방향(U, R, D, L)의 x, y 좌표 변화량을 기억하기 위한 것입니다.
- "dirs" 문자열의 각 문자에 대해 반복문을 실행합니다.
- 다음 x, y 좌표(nx, ny)를 계산합니다. "dx"와 "dy" 리스트를 통해 각 방향의 변화량을 구하고, 현재 x, y 좌표에 더합니다.
- nx, ny 좌표가 -5과 5 사이에 있는지 확인합니다.
"""
