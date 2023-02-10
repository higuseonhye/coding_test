def solution(N, stations, W):
    answer = 0
    current_station = 1
    current_index = 0
    while current_station <= N:
        if current_index < len(stations) and stations[current_index] - current_station <= W:
            current_station = stations[current_index] + W + 1
            current_index += 1
        else:
            answer += 1
            current_station += 2 * W + 1
    return answer
