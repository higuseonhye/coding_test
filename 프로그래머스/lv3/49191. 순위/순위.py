from collections import defaultdict

def solution(n, results):
    # 경기 결과 그래프 생성
    wins, loses = defaultdict(set), defaultdict(set)
    for i, j in results:
        wins[i].add(j)
        loses[j].add(i)

    # 선수별 승리 가능한 선수 집합 찾기
    for i in range(1, n + 1):
        for loser in wins[i]:
            loses[loser].update(loses[i])
        for winner in loses[i]:
            wins[winner].update(wins[i])

    # 정확한 순위를 알 수 있는 선수 카운트
    count = 0
    for i in range(1, n + 1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            count += 1

    return count

"""
경기 결과 그래프를 생성합니다. 
1. 이때, wins 딕셔너리는 각 선수가 이긴 선수의 집합을 저장하고, loses 딕셔너리는 각 선수가 진 선수의 집합을 저장합니다.
2. 모든 선수에 대해서, 승리 가능한 선수 집합과 패배 가능한 선수 집합을 각각 계산합니다. 
    이때, 이전에 계산한 승리/패배 가능한 선수 집합을 사용하여 갱신합니다.
3. 정확한 순위를 알 수 있는 선수 카운트를 구합니다. 
    이때, 선수 i의 승리/패배 가능한 선수의 수가 n-1이면, 해당 선수의 순위를 정확하게 매길 수 있습니다.
4. 구한 정확한 순위를 알 수 있는 선수 카운트를 반환합니다.
"""
