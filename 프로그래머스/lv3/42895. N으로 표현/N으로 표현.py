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
