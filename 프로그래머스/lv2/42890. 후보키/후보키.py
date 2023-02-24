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

"""
Imports the combinations function from the itertools module.

Defines a function solution that takes a single argument relation.

- Initializes variables row_len and col_len with the number of rows and columns in the relation argument.

- Creates a list candidates of all possible column combinations by iterating through each possible number of columns 
    and generating all combinations of column indices using the combinations function.

- Iterates through each combination of columns in candidates, 
    then generates a list temp of tuples by selecting the values of the corresponding columns from each row in relation. 
    
  If temp contains unique tuples for each row in relation, the combination of columns in keys is added to a list unique of unique combinations.

- Converts the list unique to a set answer and then iterates through each pair of combinations in unique. 

  If the first combination is a subset of the second combination, the second combination is removed from answer. 
  
- Returns the length of answer, which is the number of unique combinations of columns that can be used as a key in a database table.
"""
