def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    cameras = 0
    last_camera_pos = -30001
    for route in routes:
        if last_camera_pos < route[0]:
            cameras += 1
            last_camera_pos = route[1]
    return cameras
