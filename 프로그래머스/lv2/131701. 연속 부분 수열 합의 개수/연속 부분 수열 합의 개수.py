def solution(elements):
    elementLen = len(elements)
    elements = elements * 2
    sums = set()
    for i in range(elementLen):
        current_sum = 0
        for j in range(i, i + elementLen):
            current_sum += elements[j]
            sums.add(current_sum)
    return len(sums)

"""
def solution(elements):
    answer = 0
    numberSet = set()
    
    elementLen = len(elements)
    elements = elements * 2
    
    for i in range(elementLen) : 
        for j in range(elementLen) : 
            numberSet.add(sum(elements[j:j+i+1]))
    answer = len(numberSet)
    return answer
"""



