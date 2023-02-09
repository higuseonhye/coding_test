def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        s = [j for j in i if j in skill]
        if s == list(skill[:len(s)]):
            answer += 1
    return answer
