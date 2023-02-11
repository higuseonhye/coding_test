from itertools import combinations

def solution(orders, course):
    
    menu_cnt = {}   #코스요리메뉴 : 시킨 사람 수 
    for s in orders:
        for n in course:
            for i in combinations(sorted(s), n):
                print(i)
                menu_cnt[i] = menu_cnt.get(i, 0) + 1
    
    dict = { n: [2, []] for n in course }  # 키 : [시킨 사람 수, [메뉴]]
    for key in list(menu_cnt.keys()):
        if  dict[len(key)][0] == menu_cnt[key]:
            dict[len(key)][1].append(''.join(key))
        elif dict[len(key)][0] < menu_cnt[key]:
            dict[len(key)].clear()
            dict[len(key)] = [menu_cnt[key], [''.join(key)]]
            
    answer = []
    for val in dict.values():
        if val[1]:
            answer.extend(val[1])
    answer.sort()

    return answer