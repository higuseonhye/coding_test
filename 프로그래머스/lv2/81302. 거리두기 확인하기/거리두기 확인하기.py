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


"""
# Importing List from typing module
from typing import List

# Defining ROWS and COLS constants as 5
ROWS, COLS = 5, 5

# DC represents directions for columns and DR represents directions for rows
DC = [0, 0, -1, 1]
DR = [-1, 1, 0, 0]

# Defining the main function that takes a list of strings as input and returns a list of integers
def solution(places: List[str]) -> List[int]:
    
    # Initializing an empty list to store the results for each input string
    ans = []
    
    # Looping through each input string
    for place in places:
        
        # Getting a list of candidate seats to check for social distancing
        candidates = get_candidates(place)
        
        # Initializing a boolean variable to check if social distancing is maintained
        is_distancing = True
        
        # Looping through each candidate seat
        for candidate in candidates:
            
            # Checking if social distancing is maintained for the current candidate seat
            if not is_distanced(place, candidate):
                
                # If social distancing is not maintained, setting the boolean variable to False and breaking the loop
                is_distancing = False
                break
        
        # Converting the boolean result to an integer and appending it to the result list
        ans.append(int(is_distancing))
    
    # Returning the list of results
    return ans

# Function to check if social distancing is maintained for a given seat
def is_distanced(place: str, candidate: tuple, depth: int = 0, visited: List[List[bool]] = None) -> bool:
    
    # If the recursion depth exceeds 2, returning True to indicate that social distancing is maintained
    if depth > 2:
        return True
    
    # Initializing a list of visited seats if it is not provided
    if visited is None:
        visited = [[False] * COLS for _ in range(ROWS)]
    
    # Extracting the row and column indices of the current seat
    r_idx, c_idx = candidate
    
    # If the seat is outside the room, returning True to indicate that social distancing is maintained
    if r_idx < 0 or r_idx >= ROWS or c_idx < 0 or c_idx >= COLS:
        return True
    
    # If the seat has already been visited, returning True to indicate that social distancing is maintained
    if visited[r_idx][c_idx]:
        return True
    
    # If the seat is a partition, returning True to indicate that social distancing is maintained
    if place[r_idx][c_idx] == 'X':
        return True
    
    # If the seat has a person and the recursion depth is greater than 0, returning False to indicate that social distancing is not maintained
    if depth != 0 and place[r_idx][c_idx] == 'P':
        return False
            
    # Marking the current seat as visited
    visited[r_idx][c_idx] = True
    
    # Looping through each direction (up, down, left, right)
    for d_idx in range(4):
        
        # Computing the row and column indices of the adjacent seat in the current direction
        r = r_idx + DR[d_idx]
        c = c_idx + DC[d_idx]
        
        # Recursively checking if social distancing is maintained for the adjacent seat
        if not is_distanced(place, (r, c), depth=depth+1, visited=visited):
            
            # If social distancing is not maintained, returning False to indicate that social distancing is not maintained
            return False
    
    # If social distancing is maintained for
"""
