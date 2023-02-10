def solution(genres, plays):
    # Create a dictionary to store genre as key and its corresponding play counts as a list of tuples
    dic = {}
    # Iterate over the genres and plays list
    for i, genre in enumerate(genres):
        # Check if the genre already exists in the dictionary
        if genre in dic:
            # If it exists, append the current play count as a tuple with its index
            dic[genre].append((i, plays[i]))
        else:
            # If it does not exist, create a new key-value pair with the genre as key and a list containing the current play count as a tuple with its index
            dic[genre] = [(i, plays[i])]
    # Sort the values of each key in the dictionary in descending order based on the play counts
    dic = {k: sorted(v, key=lambda x: x[1], reverse=True) for k, v in dic.items()}
    # Sort the keys in the dictionary in descending order based on the sum of play counts of each genre
    dic = sorted(dic.items(), key=lambda x: sum(map(lambda y: y[1], x[1])), reverse=True)
    # Initialize an empty list to store the answer
    answer = []
    # Iterate over the sorted dictionary
    for _, lst in dic:
        # Append the first two (or less if the number of songs is less than two) indices of the genre to the answer list
        for i in range(min(len(lst), 2)):
            answer.append(lst[i][0])
    # Return the answer
    return answer

"""
주어진 리스트에서 각 장르별 재생 횟수가 가장 많은 2개의 곡의 번호를 반환하는 함수
1. 장르와 곡 번호, 재생 횟수를 담은 tuple의 list를 만든다.
2. 장르별로 재생 횟수를 기준으로 내림차순으로 정렬한다.
3. 각 장르별로 재생 횟수가 가장 많은 2개의 곡의 번호를 answer list에 담는다.
4. answer list를 반환한다.
"""
