from typing import List

ROWS, COLS = 5, 5

DC = [0, 0, -1, 1]  
DR = [-1, 1, 0, 0]  

def solution(places: List[str]) -> List[int]:
    ans = []
    for place in places:
        candidates = get_candidates(place)
        is_distancing = True
        for candidate in candidates:
            if not is_distanced(place, candidate):
                is_distancing = False
                break
        ans.append(int(is_distancing))
    return ans

def is_distanced(place: str, candidate: tuple, depth: int = 0, visited: List[List[bool]] = None) -> bool:
    if depth > 2:
        return True
    
    if visited is None:
        visited = [[False] * COLS for _ in range(ROWS)]
    
    r_idx, c_idx = candidate
    
    if r_idx < 0 or r_idx >= ROWS or c_idx < 0 or c_idx >= COLS:
        return True
    if visited[r_idx][c_idx]:
        return True
    if place[r_idx][c_idx] == 'X':
        return True
    
    if depth != 0 and place[r_idx][c_idx] == 'P':
        return False
            
    visited[r_idx][c_idx] = True
    for d_idx in range(4):
        r = r_idx + DR[d_idx]
        c = c_idx + DC[d_idx]
        if not is_distanced(place, (r, c), depth=depth+1, visited=visited):
            return False
    return True

def get_candidates(place: str) -> List[tuple]:
    candidates = []
    for r_idx in range(ROWS):
        for c_idx in range(COLS):
            if place[r_idx][c_idx] == 'P':
                candidates.append((r_idx, c_idx))
    return candidates
