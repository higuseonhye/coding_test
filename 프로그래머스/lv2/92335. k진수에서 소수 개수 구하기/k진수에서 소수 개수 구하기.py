def prime(n):
    if n <= 1: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True

def solution(n, k):
    toDigit = ""
    digit = 0
    num = 1
    while n >= num:
        num *= k
        digit += 1
    for i in range(1, digit + 1):
        digit_num = k ** (digit - i)
        toDigit += str(n // digit_num)
        n -= (n // digit_num) * digit_num

    st = []
    ans = 0
    for i in range(len(toDigit)):
        if toDigit[i] != '0':
            st.append(toDigit[i])
        else:
            if len(st) != 0:
                if prime(int(''.join(st))):
                    ans += 1
                st = []
    if len(st) != 0:
        if prime(int("".join(st))):
            ans += 1
    return ans

"""
이 코드는 n이라는 숫자를 k 진법으로 변환한 각 자릿수에서 소수가 몇 개인지 계산하는 프로그램입니다.

prime 함수는 주어진 숫자 n이 소수인지 확인하는 함수입니다.

solution 함수는 n을 k 진법으로 변환한 각 자릿수에서 소수의 개수를 계산하는 함수입니다.

digit 변수는 n이 k 진법으로 변환된 자릿수를 저장합니다.
toDigit 문자열은 n을 k 진법으로 변환한 결과를 저장합니다.
st 리스트는 toDigit에서 각 소수를 저장합니다.
ans 변수는 st에서 확인한 소수의 개수를 저장합니다.
for 문을 통해 toDigit의 각 자릿수를 순회하여, 0이 아닌 자릿수를 st에 저장하고, 0인 자릿수가 나오면 st에 저장된 숫자를 조합하여 prime 함수를 호출하여 소수인지 확인합니다.
"""

"""
prime 함수는 입력된 숫자 n이 소수인지 판별하는 함수입니다.
- n이 1보다 작거나 같은 경우 False를 반환합니다.
- 2에서 int(n ** 0.5) + 1까지 반복문을 실행하여 n이 i로 나누어 떨어지는 경우 False를 반환합니다.
- 반복문이 끝나면 True를 반환합니다.

solution 함수는 n을 k 진법으로 변환한 뒤 각 자리의 숫자가 소수인 숫자의 개수를 반환하는 함수입니다.
- digit 변수에 n을 k 진법으로 변환한 자릿수를 계산합니다.
- toDigit 변수에 n을 k 진법으로 변환한 결과를 저장합니다.
- st 리스트를 생성하여 각 자리의 숫자가 소수인 경우 누적합니다.
- toDigit의 각 자리에서 0이 아닌 경우 st 리스트에 저장합니다.
"""
