def solution(s):
    answer = []
    s = s[:-2].split('},')
    
    s = [set(map(int, i.strip('{}').split(','))) for i in s]
    
    s.sort(key=len)
	
    for tup in s:
        diff = tup - set(answer)
        answer.append(list(diff)[0])
    
    return answer

"""
이 코드는 s에서 주어진 집합들의 교집합을 찾는 기능을 구현하는 프로그램입니다.

s = s[:-2].split('},')
	문자열의 마지막 2 글자 (",}")를 제거하고 각 세트를 구분하는 '},' 기호를 기준으로 split 함수를 사용하여 리스트에 나눕니다.

s = [set(map(int, i.strip('{}').split(','))) for i in s]
	위에서 만든 리스트의 각 세트를 처리하여 정수 세트로 변환합니다. 
	각 세트에서 '{'와 '}' 기호를 제거하고 쉼표(',')를 기준으로 split 함수를 사용하여 각 요소를 분리합니다. 
	그런 다음 map 함수를 사용하여 int 형으로 변환하고 set 생성자를 사용하여 정수 세트로 변환합니다.

s.sort(key=len)
	세트의 길이에 따라 정렬하여 적은 요소를 먼저 결정하고 그 다음에 결정합니다.

for tup in s:
	각 정수 세트에 대해 반복하여 교집합을 계산합
"""
