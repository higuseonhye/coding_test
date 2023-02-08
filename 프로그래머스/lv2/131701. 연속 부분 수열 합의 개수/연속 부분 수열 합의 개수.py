def solution(elements):
    elementLen = len(elements)
    sums = set()
    for i in range(elementLen):
        current_sum = 0
        for j in range(i, i + elementLen):
            current_sum += elements[j % elementLen]
            sums.add(current_sum)
    return len(sums)
"""
첫 번째 코드는 기존의 요소를 두 배로 만들어 합계를 구하는 방식이며, 메모리를 더 많이 사용하지만 계산 횟수가 줄어듭니다.
요소의 개수가 적고 메모리 공간이 많이 필요한 경우에는 첫 번째 코드가 더 좋을 수 있습니다. 
"""
"""
이 코드는 elements 리스트의 연속한 요소의 합 중에서 유일한 합의 개수를 계산하는 프로그램입니다.
elementLen 변수에 elements 리스트의 길이를 저장합니다.
sums 세트를 생성합니다. 이 세트는 중복되지 않는 합을 저장합니다.
elementLen 만큼 반복하는 반복문을 작성합니다. 각 반복마다 current_sum 변수를 0으로 초기화합니다.
elementLen 만큼 또 다른 반복문을 작성합니다. 
    각 반복마다 j는 i에서 elementLen을 더한 값으로 증가합니다. 
    current_sum에 elements[j % elementLen]을 더합니다. 
    이는 j가 elementLen을 넘어서면 리스트의 맨 앞으로 되돌아 가도록 돕습니다.
current_sum을 sums 세트에 추가합니다.
반복문이 모두 완료되면 sums 세트의 길이를 반환하여 유일한 합의 개수를 나타냅니다.
"""



"""
두 번째 코드는 기존의 요소를 그대로 사용하지만, 메모리를 적게 사용하지만 계산 횟수가 늘어납니다.
요소의 개수가 많고 메모리 공간이 적은 경우에는 두 번째 코드가 더 좋을 수 있습니다.
"""
def solution(elements):
    elementLen = len(elements)
    elements = elements * 2
    sums = set()
    for i in range(elementLen):
        current_sum = 0
        for j in range(i, i + elementLen):
            current_sum += elements[j]
            sums.add(current_sum)
    return len(sums)
"""
주어진 elements 리스트의 길이를 elementLen에 저장합니다. 
그 다음 elements 리스트를 2배 길이로 복사해서 변수 elements에 저장합니다.

그 다음, sums set을 생성하여 각 sublist의 합을 저장합니다.

for 루프를 elementLen만큼 돌면서 current_sum 변수를 0으로 초기화합니다. 또 다른 for 루프를 돌면서 i와 i + elementLen 사이의 원소의 합을 계산합니다. 
계산된 결과를 current_sum에 더하고, sums set에 저장합니다.

마지막으로, sums set의 크기(원소의 개수)를 반환합니다.
"""
