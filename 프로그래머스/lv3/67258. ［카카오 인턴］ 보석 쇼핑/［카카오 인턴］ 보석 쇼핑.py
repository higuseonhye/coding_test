def solution(gems):
    gem_types = len(set(gems))
    gem_count = len(gems)
    gem_dict = {gems[0]: 1}
    solutions = []
    left_index, right_index = 0, 0
    while left_index < gem_count and right_index < gem_count:
        if len(gem_dict) < gem_types:
            right_index += 1
            if right_index == gem_count:
                break
            gem_dict[gems[right_index]] = gem_dict.get(gems[right_index], 0) + 1
        else:
            solutions.append((right_index-left_index + 1, [left_index+1, right_index+1]))
            gem_dict[gems[left_index]] -= 1
            if gem_dict[gems[left_index]] == 0:
                del gem_dict[gems[left_index]]
            left_index += 1
    solutions.sort(key=lambda x: (x[0], x[1]))
    return solutions[0][1]