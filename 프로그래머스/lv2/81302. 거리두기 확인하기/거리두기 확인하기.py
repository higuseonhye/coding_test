from typing import List


ROWS, COLS = 5, 5

#     상   하  좌  우
DC = [ 0, 0, -1, 1]
DR = [-1, 1,  0, 0]


def solution(places):
    global visited
    
    ans = []
    for place in places:
        candidates = get_candidates(place)
        is_distancing = True
        for candidate in candidates:
            visited = [[False] * COLS for _ in range(ROWS)]
            if not dfs(place, candidate):
                is_distancing = False
                break
                
        ans.append(int(is_distancing))
    return ans


def dfs(place:list, candidate:tuple, depth:int=0) -> bool:
    # depth == 현재 탐색 중인 거리값(Current distance)
    if depth > 2:
        return True
    
    r_idx, c_idx = candidate
    if r_idx < 0 or r_idx >= ROWS or c_idx < 0 or c_idx >= COLS:  # Ignore: Out of index
        return True
    if visited[r_idx][c_idx]:  # Ignore: Already visited node
        return True
    if place[r_idx][c_idx] == 'X':  # Ignore: 'X'(파티션)
        return True
    
    # 거리값 2 이내의 응시자 존재 --> Fail
    if depth != 0 and place[r_idx][c_idx] == 'P':
        return False
            
    visited[r_idx][c_idx] = True
    for d_idx in range(4):  # 상, 하, 좌, 우
        r = r_idx + DR[d_idx]
        c = c_idx + DC[d_idx]
        if not dfs(place, (r, c), depth=depth+1):
            return False
    return True


def get_candidates(place:list) -> List[tuple]:
    candidates = []
    for r_idx in range(ROWS):
        for c_idx in range(COLS):
            if place[r_idx][c_idx] == 'P':
                candidates.append((r_idx, c_idx))
    return candidates