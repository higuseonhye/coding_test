def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)] # 튜플로 만들어줌 (문서의 위치, 중요도)
    answer = 0
    while queue:
        document = queue.pop(0)
        if any(document[1] < q[1] for q in queue): # 대기 목록에 있는 문서들 중 하나라도 현재 문서보다 중요도가 높으면 
            queue.append(document) # 맨 뒤로 보냄
        else:
            answer += 1 # 인쇄
            if document[0] == location: # 원하는 문서이면
                return answer # 결과 반환

"""
이 코드는 프린터 큐에서 문서의 인쇄 순서를 구하는 알고리즘입니다.

"priorities" 리스트와 "location" 값을 인수로 받습니다.
"queue" 리스트를 생성하여 각 문서의 위치와 중요도를 튜플로 저장합니다.
"answer" 변수를 초기화하여 프린트 된 문서의 수를 저장합니다.
"queue" 리스트가 빌 때까지 반복하여, 가장 앞에 있는 문서를 꺼내어 현재 문서의 중요도가 나머지 대기 목록에 있는 문서의 중요도보다 낮으면, 맨 뒤로 이동시킵니다.
현재 문서의 중요도가 높을 경우, "answer" 변수를 1 증가시키고, 현재 문서가 원하는 문서일 경우, "answer" 값을 반환합니다.
"""
