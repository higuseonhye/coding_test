def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    cameras = 0
    last_camera_pos = -30001
    for route in routes:
        if last_camera_pos < route[0]:
            cameras += 1
            last_camera_pos = route[1]
    return cameras

"""
이 코드는 "단속카메라" 문제의 해답을 구하는 파이썬 코드입니다.

우선, 주어진 routes 리스트를 route[1]을 기준으로 정렬합니다. 
- 이는 차량이 고속도로를 떠나는 순서대로 정렬하기 위함입니다.

그 다음, cameras 변수를 0으로 초기화하고, last_camera_pos 변수를 -30001로 초기화합니다. 
- 이 변수는 마지막에 설치된 카메라의 위치를 저장하는 변수입니다.

그 다음, routes 리스트에서 각 route를 하나씩 꺼내서 처리합니다. 
- 만약 last_camera_pos가 현재 route의 진입점인 route[0] 보다 작은 경우(즉, 현재 차량을 단속하기 위해서는 새로운 카메라가 필요한 경우), 
    cameras를 1 증가시키고, last_camera_pos를 현재 route의 진출점인 route[1]로 갱신합니다.

마지막으로, cameras 변수를 반환합니다. 이 값은 최소한으로 단속하기 위해서 필요합니다.
"""
