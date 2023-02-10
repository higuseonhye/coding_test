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
