import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    while scoville[0] < K and len(scoville) != 1:
        v = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, v)
        cnt += 1

    return -1 if scoville[0] < K else cnt

"""
이 파이썬 코드는 solution 함수를 정의하고 있습니다. 이 함수의 입력은 두 개의 매개변수 scoville와 K입니다.

함수는 첫 번째 매개변수 scoville의 각 요소를 기준으로 어떤 음식이 얼마나 매운지 측정하고 있습니다. 
음식의 매운 정도는 작은 값으로 표시됩니다.

두 번째 매개변수 K는 최소한 몇 점의 매운 정도를 가진 음식이 필요한지 나타냅니다.

함수 내부에서, heapq.heapify(scoville)는 scoville 리스트를 최소 힙으로 변환합니다. 
이는 scoville 리스트에서 최소값을 빠르게 찾을 수 있도록 합니다.

그리고, 루프를 실행하며, scoville[0]이 K 보다 작고 scoville 리스트의 길이가 1이 아닐 때까지 수행됩니다.

루프 안에서, v는 힙에서 두 개의 최소값을 꺼내서 더한 것과 2배한 값입니다. 
"""
