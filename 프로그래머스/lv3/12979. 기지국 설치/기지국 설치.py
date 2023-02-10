def solution(N, stations, W):
    # Initialize a variable to store the answer
    answer = 0
    # Initialize the first apartment to be covered
    current_station = 1
    # Initialize the current index of the station
    current_index = 0
    # Loop until all apartments are covered
    while current_station <= N:
        # If the current station can cover the current apartment
        if current_index < len(stations) and stations[current_index] - current_station <= W:
            # Update the current station to be the next station
            current_station = stations[current_index] + W + 1
            # Move on to the next station
            current_index += 1
        else:
            # If the current station cannot cover the current apartment, increase the number of required stations
            answer += 1
            # Update the current station to be W units away from the current apartment
            current_station += 2 * W + 1
    # Return the final answer
    return answer

"""
This solution uses two pointers to keep track of the current station and the current index in the stations array. 
- The while loop continues until all the apartments have received the signal. 
- If the current apartment has a station within the reach of W, the current station is updated to be the next station plus W + 1. 
- If not, the answer is incremented and the current station is updated to be the next possible station, which is the current station plus 2 * W + 1.
"""