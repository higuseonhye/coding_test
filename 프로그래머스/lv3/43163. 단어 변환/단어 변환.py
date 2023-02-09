from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    n = len(begin)
    words = set(words)
    q = deque([(begin, 0)])
    while q:
        word, step = q.popleft()
        if word == target:
            return step
        for i in range(n):
            for j in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + j + word[i+1:]
                if next_word in words:
                    q.append((next_word, step + 1))
                    words.remove(next_word)
                    break

    return 0

"""
이 코드는 "알파벳 변환" 문제를 해결하는 BFS (Breadth-First Search) 알고리즘을 구현한 것입니다.

begin: 시작 단어
target: 목표 단어
words: 변환 가능한 단어 목록

- target 단어가 words 목록에 없는 경우 0을 반환합니다.
- begin 단어의 길이(n)와 words 목록을 set으로 변환합니다.
- BFS 구현을 위해 deque 라이브러리에서 가져온 queue를 생성합니다. 첫 번째 원소로 (begin, 0)을 추가합니다.
- queue가 빌 때까지 계속해서 반복합니다.
    a. queue에서 word와 step을 꺼냅니다.
    b. word가 target이면 step을 반환합니다.
    c. word의 각 문자를 순회하며, a~z의 문자로 변환 후 next_word를 생성합니다.
    d. next_word가 words 목록에 포함되어 있으면, (next_word, step + 1)을 queue에 추가하고 words에서 제거합니다.
- queue가 비고 0이 반환된 경우 (target 단어에 도달할 수 없는 경우) 0을 반환합니다.
"""
