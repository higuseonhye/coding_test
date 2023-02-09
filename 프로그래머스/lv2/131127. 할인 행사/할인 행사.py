def solution(want, number, discount):
    ans = 0
    wantList = dict(zip(want, number))
    wantSet = set(want)

    for j in range(len(discount)):
        if discount[j] in wantList:
            wantList[discount[j]] -= 1
            if wantList[discount[j]] == 0:
                wantSet.remove(discount[j])

        if j >= 10:
            if discount[j-10] in wantList:
                wantList[discount[j-10]] += 1
                if wantList[discount[j-10]] == 1:
                    wantSet.add(discount[j-10])

        if len(wantSet) == 0:
            ans+=1 

    return ans

"""
이 Python 코드는 주어진 want, number, discount 리스트를 사용하여 할인 기회가 몇 번 있었는지 계산하는 프로그램입니다.

ans 변수를 0으로 초기화하고, wantList 딕셔너리와 wantSet 집합을 생성합니다. 
wantList 딕셔너리는 want 리스트와 number 리스트의 값을 매핑하여 생성되고, wantSet 집합은 want 리스트의 값을 저장합니다.

discount 리스트에서 각 할인 기회에 대해 반복문을 실행합니다.

현재 할인 기회에 해당하는 아이템이 wantList에 있는 경우, 해당 아이템의 수량을 1 감소시키고, 수량이 0이 되었을 경우 wantSet에서 해당 아이템을 제거합니다.

현재 할인 기회의 인덱스가 10 이상인 경우, 10 개 전의 할인 기회에 해당하는 아이템을 wantList에서 검색하고, 수량을 1 증가시키고, 
수량이 1이 되었을 경우 wantSet에 해당 아이템을 추가
"""
"""
wantList와 wantSet을 초기화합니다. 
    wantList는 want와 number 목록을 매핑하는 사전이고, wantSet은 wantList에서 남아 있는 물건의 목록을 나타냅니다.
for 루프를 사용하여 discount 목록을 순회합니다.
각 물건이 wantList에 있는지 확인합니다. 
    있다면, 해당 물건에 대한 구입 요구 수를 1 감소시킵니다. 구입 요구 수가 0이 된다면, wantSet에서 해당 물건을 제거합니다.
"""
"""
solution 함수를 정의합니다. want과 number, discount라는 3개의 인자가 입력됩니다.
ans라는 변수를 0으로 초기화하고, 결과값을 담을 변수입니다.
wantList 딕셔너리를 생성하고 want 리스트와 number 리스트를 사용하여 구성합니다.
wantSet으로 want 리스트를 set으로 변환합니다.
discount 리스트를 순회하며, 각 상품을 구매하는 과정을 반복합니다.
구매할 상품이 wantList에 있을 경우, 해당 상품의 수량을 1 감소시킵니다.
감소된 상품의 수량이 0이 될 경우, wantSet에서 해당 상품을 제거합니다.
"""
