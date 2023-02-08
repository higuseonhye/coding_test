import heapq

def solution(n, works):
    for i in range(len(works)):
        works[i] *= -1
    heapq.heapify(works)

    for i in range(0, n):
        m = heapq.heappop(works)
        if m >= 0:
            heapq.heappush(works, m)
            break
        m += 1
        heapq.heappush(works, m)

    answer = 0
    while len(works) > 0:
        m = heapq.heappop(works)
        answer += pow(m * -1, 2)
    return answer

"""
works 배열의 각 아이템에 -1을 곱합니다. 이는 works 배열을 최소 힙 구조로 변환하는 것입니다.
heapq 라이브러리를 사용하여 최소 힙 구조를 생성합니다.
n번 반복하여 works 배열에서 가장 작은 값을 가져옵니다. 그런 다음, 값을 1 증가시키고 다시 works 배열에 삽입합니다.
works 배열이 빌 때까지 계속해서 가장 작은 값을 가져와 answer 변수에 곱해 (m * -1)^2를 더합니다.
최종 answer 값을 반환합니다.
"""
