def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        s = [j for j in i if j in skill]
        if s == list(skill[:len(s)]):
            answer += 1
    return answer

"""
이 코드는 주어진 skill 문자열과 skill_trees 리스트에서 얼마나 많은 skill_tree가 skill의 순서에 맞게 스킬을 가지고 있는지 계산하는 것이다.

answer 변수를 0으로 초기화한다. 이 변수는 skill_tree가 skill의 순서에 맞게 스킬을 가지고 있을 때마다 1씩 증가할 것이다.

반복문을 사용하여 skill_trees 리스트에서 각 skill_tree를 검사한다.

반복문의 현재 skill_tree에서 skill 문자열에 포함된 문자만 골라서 리스트 s에 저장한다.

s 리스트가 skill[:len(s)]와 같은지 확인한다. 이 확인은 skill_tree가 skill의 순서에 맞게 스킬을 가지고 있는지를 검사한다. 만약 같다면, answer 변수를 1 증가시킨다.

모든 skill_tree를 검사한 후, answer 변수를 반환한다.
"""
