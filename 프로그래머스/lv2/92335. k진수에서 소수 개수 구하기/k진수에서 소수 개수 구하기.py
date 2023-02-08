def prime(n):
    if n <= 1: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True

def getDigit(n, k):
    digit = 0
    num = 1
    while n >= num:
        num *= k
        digit+=1
    return digit

def solution(n, k):
    toDigit = ""
    digit = getDigit(n, k)
    while digit > 0:
        digitNum = k**(digit-1)
        if k**(digit-1) <= n:
            toDigit += str((n//digitNum))
            n -= ((n//digitNum)*digitNum)
        else:
            toDigit += '0'
        digit -= 1

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
