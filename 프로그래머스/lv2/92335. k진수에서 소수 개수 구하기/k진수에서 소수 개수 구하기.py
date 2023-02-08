def setIsPrime():
    MAX_NUM = 60000001
    isPrime = [True for i in range(MAX_NUM)]

    isPrime[0] = False
    isPrime[1] = False
    isPrime[2] = True
    for i in range(2,MAX_NUM):
        if isPrime[i] == True:
            for j in range(2,(MAX_NUM//(i))):
                isPrime[i*j] = False
    return isPrime

def prime(n):
    if n <= 1: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True

# 진수로 변환해주는 함수
def getDigit(n, k):
    digit = 0
    num = 1
    while n >= num:
        num *= k
        digit+=1
    return digit # 자리수 4개

def solution(n, k):


    toDigit = ""
    digit = getDigit(n,k)
    while digit > 0:
        digitNum = k**(digit-1)
        if k**(digit-1) <= n:
            toDigit += str((n//digitNum))
            n -= ((n//digitNum)*digitNum)
        else:
            toDigit += '0'
        digit -= 1

    # ------- 진수 변환 끝
    """
    0P0소수 양쪽에 0이 있는 경우
    P0 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
    0P 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
    """
    st = []
    ans = 0

    for i in range(len(toDigit)):
        if toDigit[i] != '0':
            st.append(toDigit[i])
        else:
            if len(st) != 0:

                if prime(int(''.join(st))):
                    ans+=1
                st = []

    if len(st) != 0:
        if prime(int("".join(st))):
            ans+=1

    return ans