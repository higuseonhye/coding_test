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
