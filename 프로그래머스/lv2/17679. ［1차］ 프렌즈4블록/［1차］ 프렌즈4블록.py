def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])
    
    cnt = 0
    rm = set()
    while True:
        # 보드를 순회하며 4블록이 된 곳의 좌표를 집합에 기록
        for i in range(m-1):
            for j in range(n-1):
                t = board[i][j]
                if t == []:
                    continue
                if board[i+1][j] == t and board[i][j+1] == t and board[i+1][j+1] == t:
                    rm.add((i,j));rm.add((i+1,j))
                    rm.add((i,j+1));rm.add((i+1,j+1))
        
        # 좌표가 존재한다면 집합의 길이만큼 세주고 블록을 지움 
        if rm:
            cnt += len(rm)
            for i,j in rm:
                board[i][j] = []
            rm = set()
        # 없다면 함수 종료
        else:
            return cnt
        
        # 블록을 위에서 아래로 당겨줌
        while True:
            moved = 0
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and board[i+1][j]==[]:
                        board[i+1][j] = board[i][j]
                        board[i][j] = []
                        moved = 1
            if moved == 0:
                break
                
"""
이 코드는 게임 보드에서 4개의 블록을 제거하는 프로그램입니다. 입력된 m, n, board 매개변수에 따라서 게임 보드의 크기와 내용이 결정됩니다.
- 우선, board 리스트의 각 항목을 리스트 형식으로 변환하여 준비합니다.
- 그 다음, 게임 보드를 순회하며 4개의 블록이 된 곳의 좌표를 rm 집합에 기록합니다.
- 만약 rm 집합에 좌표가 존재한다면, 집합의 길이만큼 카운트 값을 증가시키고 board에서 지웁니다.
- 만약 좌표가 존재하지 않는다면, 함수를 종료하고 카운트 값을 반환합니다.
- 마지막으로, board에서 블록을 위에서 아래로 당겨줍니다. 이 과정은 빈 공간이 생겼을 때 계속 수행되며, 블록이 움직일 수 없을 때까지 수행합니다.
"""
"""
m: 2차원 보드의 행(row) 수
n: 2차원 보드의 열(column) 수
board: 2차원 보드의 각 칸의 상태를 나타내는 문자열의 리스트

함수는 먼저 board 리스트의 각 행을 리스트로 변환합니다.
- 그런 다음, 함수는 "cnt"라는 변수를 초기화하고 "rm"이라는 집합을 생성합니다. 그리고 루프를 순회하며 board의 각 칸을 검사하여 4개의 동일한 블록이 나열되어 있는 곳의 좌표를 rm 집합에 기록합니다.
- 만약 rm 집합에 좌표가 존재한다면, 그 집합의 길이만큼 "cnt"를 증가시키고 rm 집합에 기록된 좌표에 있는 블록을 지웁니다.
- 만약 rm 집합에 좌표가 없다면 함수를 종료하여 "cnt" 값을 반환합니다.
"""
