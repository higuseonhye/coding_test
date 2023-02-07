def solution(k, tangerine):
    tmp_list = []

    # 리스트 처리를 위해 sort()를 활용하여 같은 숫자끼리 붙어있게 처리
    tangerine.sort()
    # 초기 카운트 (중복 개수 세기)
    cnt = 1
    for i in range(len(tangerine)):
        # 마지막 숫자일 경우 현재까지 cnt 개수와 마지막 숫자 저장
        if i == len(tangerine) - 1:
            tmp_list.append([tangerine[i], cnt])
        # 리스트 다음 인덱스 숫자와 비교하여 같으면 cnt 숫자 증가
        elif tangerine[i] == tangerine[i + 1]:
            cnt += 1
        # 다를 경우 현재까지 cnt와 해당 숫자 저장
        else :
            tmp_list.append([tangerine[i], cnt])
            cnt = 1
            
    # 저장된 리스트에서 카운트 크기순으로 정렬 
    tmp_list.sort(key = lambda x:-x[1])    

    total = 0
    result = 0

    # 카운트 크기순으로 더하고 만약 그 크기가 k를 넘어갈 경우 break하고 결과 출력
    for info in tmp_list:
        total += info[1]
        result += 1
        if k <= total :
            break       

    answer = result
    return answer