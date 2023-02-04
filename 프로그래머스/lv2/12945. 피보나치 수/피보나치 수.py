"""
루프 방식으로 구현하면 재귀적인 호출을 피하여 효율적으로 계산할 수 있습니다. 
또한, 1234567으로 나눈 나머지를 계산하기 위해서 % 연산자를 사용하여 값을 제한하고 있습니다.
"""

def solution(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for i in range(2, n+1):
        c = (a + b) % 1234567
        a, b = b, c

    return b



"""
이 코드는 피보나치 수열의 각 숫자를 생성하는 generator 함수입니다. 
yield 키워드를 사용하여 피보나치 숫자를 생성하고, 지정한 숫자까지만 계산하게 됩니다. 
이 방식은 미리 전체 리스트를 계산하지 않고 필요한 숫자만 계산하는 효율적인 방식입니다.

def fibonacci(number):
    yield 1
    if number == 0:
        return

    prev, now = 1, 1
    for _ in range(1, number):
        yield now
        now, prev = now + prev, now

assert list(fibonacci(10)) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
assert sum(fibonacci(5)) == 12
print("통과") 
"""



"""
이 코드의 경우, 피보나치 수열을 재귀적으로 계산하기 때문에 같은 값을 반복해서 계산하게 됩니다. 
def fib(num):
    """ Print the nth number in the fibonacci sequence """
    if num <= 1:
        return num
    else:
        return fib(num-1) + fib(num-2)
print(fib(10))
"""




