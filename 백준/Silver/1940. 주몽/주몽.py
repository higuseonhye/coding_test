n = int(input().strip())
m = int(input().strip())
a = [int(i) for i in input().strip().split()]

cnt = 0
for i in a:
    if m-i in a:
        cnt += 1

print(cnt//2)

"""
이 코드는 주어진 리스트 'a'에서 두 요소의 합이 'm'인 쌍의 개수를 셈하는 프로그램입니다.

'n'과 'm'을 입력 받고, 'a' 리스트를 공백을 기준으로 입력받습니다.
'cnt' 변수를 초기화합니다.
'a' 리스트의 각 요소 'i'에 대해, 'm-i' 값이 'a'에 존재하면 'cnt'를 1 증가시킵니다.
'cnt'를 2로 나눈 후 결과를 출력합니다. (중복 셈 방지)
"""
