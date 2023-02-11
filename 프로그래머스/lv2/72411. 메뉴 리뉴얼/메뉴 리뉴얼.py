from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for n in course:
        menu = []
        for order in orders:
            menu += list(combinations(sorted(order), n))
        menu_counts = Counter(menu)
        max_count = 2
        for menu_item, count in menu_counts.most_common():
            if count > max_count:
                answer.append(''.join(menu_item))
                max_count = count
            elif count == max_count:
                answer.append(''.join(menu_item))
            else:
                break
    answer.sort()
    return answer
