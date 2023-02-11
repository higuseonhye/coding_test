from itertools import combinations
from collections import Counter

def solution(orders, course):

    answer = []
    
    for n in course:
        menu = []
        for s in orders:
            menu += list(combinations(sorted(s), n))
        menu_cnt_s = Counter(menu).most_common()
        max_cnt = 2
        for menu_cnt in menu_cnt_s:
            if menu_cnt[1] > max_cnt:
                answer.append(''.join(menu_cnt[0]))
                max_cnt = menu_cnt[1]
            elif menu_cnt[1] == max_cnt:
                answer.append(''.join(menu_cnt[0]))
            else:
                break
    
    answer.sort()
    
    return answer