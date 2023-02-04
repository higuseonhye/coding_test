def solution(n, words):
    used_words = []
    for i, word in enumerate(words):
        if word in used_words or (i > 0 and word[0] != words[i - 1][-1]):
            return [(i % n) + 1, (i // n) + 1]
        used_words.append(word)
    return [0, 0]
