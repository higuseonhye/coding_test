def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] <= i:
            return i
    return len(citations)

"""
This code sorts the given citations array in descending order, then iterates over it. 
For each iteration, it checks if the current value is less than or equal to the current index. 
If this condition is satisfied, it returns the current index. 
If the iteration completes, it returns the length of the citations array.
"""
