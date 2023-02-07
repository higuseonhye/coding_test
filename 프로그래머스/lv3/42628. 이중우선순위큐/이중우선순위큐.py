from heapq import heappush, heappop

def solution(operations):
    min_heap = []
    max_heap = []
    
    for op in operations:
        cmd, num = op.split()
        num = int(num)
        if cmd == "I":
            heappush(min_heap, num)
            heappush(max_heap, -num)
        elif num == 1 and max_heap:
            max_num = -heappop(max_heap)
            min_heap.remove(max_num)
        elif num == -1 and min_heap:
            min_num = heappop(min_heap)
            max_heap.remove(-min_num)
    
    if not min_heap:
        return [0, 0]
    else:
        return [-max_heap[0], min_heap[0]]
