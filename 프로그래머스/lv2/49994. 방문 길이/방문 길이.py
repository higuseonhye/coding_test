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
