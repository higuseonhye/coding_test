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