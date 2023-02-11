def solution(gems):
    gem_types = set(gems)
    gem_count = len(gems)
    type_count = len(gem_types)

    current_shop = {gems[0]: 1}
    candidates = []
    left_index, right_index = 0, 0

    while left_index < gem_count and right_index < gem_count:
        if len(current_shop) < type_count:
            right_index += 1
            if right_index == gem_count:
                break
            current_shop[gems[right_index]] = current_shop.get(gems[right_index], 0) + 1
        else:
            distance = right_index - left_index
            candidate = [left_index + 1, right_index + 1]
            candidates.append((distance, candidate))
            current_shop[gems[left_index]] -= 1
            if current_shop[gems[left_index]] == 0:
                del current_shop[gems[left_index]]
            left_index += 1

    candidates.sort(key=lambda x: (x[0], x[1]))

    return candidates[0][1]