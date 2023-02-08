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