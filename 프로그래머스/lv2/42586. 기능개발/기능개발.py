def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        if cnt > 0:
            answer.append(cnt)
    return answer

"""
이 코드는 개발 작업의 진척 상황을 나타내는 리스트 progresses와 각 작업의 속도를 나타내는 리스트 speeds를 입력으로 받아 
    각 작업이 완료되는 날짜를 계산하고, 같은 날짜에 완료된 작업의 개수를 반환하는 함수입니다.

1. cnt 변수를 초기화합니다.
2. progresses 리스트가 비어 있지 않은 동안 반복합니다.
3. progresses 리스트의 각 요소를 speeds 리스트에 대응하는 요소에 해당하는 값만큼 증가시킵니다.
4. progresses 리스트가 비어 있지 않고 progresses[0] >= 100인 경우 progresses와 speeds 리스트의 첫 번째 요소를 제거하고 cnt 변수의 값을 1 증가시킵니다.
5. cnt 값이 0보다 큰 경우 answer 리스트에 cnt 값을 추가합니다.
6. progresses 리스트가 비어지면 반복을 중단합니다.
7. answer 리스트를 반환합니다.
"""

"""
def solution(progresses, speeds):
    answer = []
    cnt = 0
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        if cnt > 0:
            answer.append(cnt)
            cnt = 0
    return answer

두번째 코드에서는 함수가 실행될 때마다 cnt 변수의 값이 초기화되지 않고 계속 유지되기 때문에 예상치 못한 결과가 나올 수 있습니다. 
반면, 첫번째 코드에서는 각 루프 마다 cnt 변수의 값이 초기화되기 때문에 예상치 못한 결과가 나오지 않습니다.

따라서 첫번째 코드가 더 효율적이고, 보다 안정적이며 오류가 덜한 코드입니다.
"""
