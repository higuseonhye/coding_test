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
