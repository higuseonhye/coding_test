from itertools import combinations

def solution(relation):
    row_len = len(relation)
    col_len = len(relation[0])
    # Create a list of all possible column combinations
    candidates = []
    for i in range(1, col_len + 1):
        candidates.extend(combinations(range(col_len), i))
    # Check for uniqueness of each column combination
    unique = []
    for keys in candidates:
        temp = [tuple(row[key] for key in keys) for row in relation]
        if len(set(temp)) == row_len:
            unique.append(keys)
    # Remove redundant column combinations
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if set(unique[i]).issubset(set(unique[j])):
                answer.discard(unique[j])
    return len(answer)
