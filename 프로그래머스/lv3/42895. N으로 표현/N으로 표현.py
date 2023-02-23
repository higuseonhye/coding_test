def solution(N, number):
    # 각 숫자마다 만들 수 있는 숫자 집합 초기화
    possible_nums = [set() for _ in range(9)]
    for i in range(1, 9):
        possible_nums[i].add(int(str(N) * i))

    # 사칙연산을 통해 만들 수 있는 숫자 찾기
    for i in range(1, 9):
        for j in range(1, i):
            for x in possible_nums[j]:
                for y in possible_nums[i - j]:
                    possible_nums[i].add(x + y)
                    possible_nums[i].add(x - y)
                    possible_nums[i].add(y - x)
                    possible_nums[i].add(x * y)
                    if y != 0:
                        possible_nums[i].add(x // y)
                    if x != 0:
                        possible_nums[i].add(y // x)

        if number in possible_nums[i]:
            return i

    return -1

"""
해당 코드는 다음과 같이 동작합니다.

1. 각 숫자마다 만들 수 있는 숫자 집합을 초기화합니다. 
    이때, i번째 숫자 집합에는 i번 N을 사용하여 만들 수 있는 숫자의 집합을 저장합니다.
2. 1부터 8까지 숫자 i에 대해서, j와 i-j를 사용하여 가능한 모든 연산을 수행하여 만들 수 있는 숫자를 추가합니다.
3. 만약 number가 i번째 숫자 집합에 있다면, N 사용 횟수의 최솟값이 i이므로 i를 반환합니다.
4. 모든 숫자 집합에 대해 탐색하고도 number를 만들 수 없다면, -1을 반환합니다.

숫자 집합을 만드는 부분에서는 다음과 같은 사항들에 유의해야 합니다.

1. i번째 숫자 집합을 만들 때, j와 i-j를 사용하여 만들 수 있는 모든 연산을 수행합니다.
2. 숫자를 이어 붙이는 경우는 str(N) * i와 같이 문자열을 사용하여 만들 수 있습니다.
3. 나누기 연산에서 나머지는 무시하므로, y가 0인 경우에는 나누기 연산을 수행하지 않습니다.
4. 0으로 나눌 수 없으므로, x가 0인 경우에는 나누기 연산을 수행하지 않습니다.
"""
