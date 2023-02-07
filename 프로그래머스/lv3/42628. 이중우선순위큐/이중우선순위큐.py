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

"""
This is a Python3 code that implements a solution to a problem where the goal is to maintain a data structure that can support two operations: 
    adding a number, and removing the largest or smallest number. 
The code uses two heaps, a min-heap and a max-heap, to efficiently keep track of the smallest and largest numbers, respectively.

The operations are passed as a list of strings, where each string consists of a command ("I" for insert or "+/-1" for remove) and a number. 
The code iterates through the operations, executing the corresponding actions based on the command. When inserting a number, 
    the number is added to both the min-heap and max-heap. When removing the largest number, the code pops the largest element
"""
"""
이 Python3 코드는 최솟값과 최댓값을 관리하는 문제에 대한 해결책을 구현한 것입니다. 
최솟값과 최댓값을 관리하기 위해서는 min-heap과 max-heap이라는 2개의 힙을 사용합니다.

작업은 문자열의 리스트로 전달되며, 각 문자열은 명령("I"는 삽입, "+/-1"은 제거)과 숫자로 구성됩니다. 
코드는 작업을 반복하여 명령에 따라 알맞은 작업을 수행합니다. 숫자를 삽입할 때에는 min-heap과 max-heap에 모두 숫자를 추가합니다. 
최댓값을 제거할 때에는 max-heap에서 가장 큰 요소를 pop하여 to_delete 집합에 추가합니다. 
최솟값을 제거할 때에는 min-heap에서 가장 작은 요소를 pop하여 to_delete 집합에 포함되지 않으면 max-heap에 넣습니다.

마지막으로, min-heap과 max-heap에서 to_delete 집합에 포함된 요소를 제거합니다. min-heap이 비어있으면 [0, 0]을 반환
"""
