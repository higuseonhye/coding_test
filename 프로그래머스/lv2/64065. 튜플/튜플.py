def solution(s):
    answer = []
    s = s[:-2].split('},')
    
    s = [set(map(int, i.strip('{}').split(','))) for i in s]
    
    s.sort(key=len)
	
    for tup in s:
        diff = tup - set(answer)
        answer.append(list(diff)[0])
    
    return answer

