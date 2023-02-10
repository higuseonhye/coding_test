from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque([0] * bridge_length)
    bridge_weight = 0
    sec = 0
    while truck_weights:
        sec += 1
        bridge_weight -= q.popleft()
        if bridge_weight + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            q.append(truck)
            bridge_weight += truck
        else:
            q.append(0)
    return sec + bridge_length

"""
이 코드는 트럭이 다리를 건너는데 걸리는 최소 시간을 계산하는 프로그램입니다.

1. from collections import deque 라인에서 deque 모듈을 가져왔습니다. deque 모듈은 큐(queue) 데이터 구조를 제공하는 모듈입니다.
2. solution 함수는 3개의 인자를 받습니다. 
    - bridge_length 는 다리의 길이, weight 는 다리가 견딜 수 있는 최대 무게, truck_weights 는 트럭의 무게를 나타내는 리스트입니다.
3. q 변수에 deque 객체를 할당합니다. 
    - 이 객체는 bridge_length 만큼의 0으로 구성된 리스트를 갖습니다. 이 큐는 현재 다리위에 있는 트럭들을 나타냅니다.
4. bridge_weight 변수는 현재 다리위의 트럭들의 총 무게를 나타냅니다.
5. sec 변수는 현재까지 걸린 시간을 나타냅니다.
6. while truck_weights 루프는 truck_weights 리스트가 빌 때까지 반복합니다. 
"""
