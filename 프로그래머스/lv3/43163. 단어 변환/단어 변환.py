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

    return 0
