def solution(people, limit):
    people.sort()
    i, j = 0, len(people) - 1
    count = 0
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        count += 1
    return count

"""
people 리스트를 오름차순으로 정렬 후, 가장 작은 값(people[i])와 가장 큰 값(people[j])을 검사하여 두 값의 합이 limit 이하이면 i를 1 증가시키고, 
     j를 1 감소시켜 구명보트의 개수(count)를 1 증가시킵니다. 
이 과정을 반복하여 모든 사람을 구출할 때까지 구명보트의 개수를 계산하여 return합니다.
"""
