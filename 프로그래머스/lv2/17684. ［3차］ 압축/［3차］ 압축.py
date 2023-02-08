def solution(msg):
	dic = {chr(65 + i): i + 1 for i in range(26)}
	cur_str = ""
	result = []
	for c in msg:
		temp = cur_str + c
		if temp in dic:
			cur_str = temp
		else:
			result.append(dic[cur_str])
			dic[temp] = len(dic) + 1
			cur_str = c
	if cur_str:
		result.append(dic[cur_str])
	return result

"""
주어진 코드는 문자열을 압축하는 프로그램입니다.

dic은 26개의 문자(A-Z)에 대한 숫자(1-26) 매핑을 포함하는 딕셔너리입니다.
cur_str은 현재 압축중인 문자열입니다.
result는 압축된 결과를 저장할 리스트입니다.
for c in text는 text의 각 문자에 대해 반복하는 루프입니다.
- temp는 cur_str에 c를 추가한 것입니다.
- if temp in dic은 temp가 dic에 존재하는지 검사합니다.
- temp가 dic에 존재하면 cur_str을 temp로 업데이트합니다.
- else는 temp가 dic에 존재하지 않는 경우입니다.
- result에 dic[cur_str]을 추가합니다.
- dic에 temp와 len(dic) + 1을 매핑하는 값을 추가합니다.
- cur_str을 c로 업데이트합니다.
if cur_str:은 cur_str이 비어 있지 않은 경우입니다.
- result에 dic[cur_str]을 추가합니다.
return result는 result를 반환합니다.
"""
