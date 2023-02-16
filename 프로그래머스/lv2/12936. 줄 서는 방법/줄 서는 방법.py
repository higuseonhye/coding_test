import math

def solution(n, k):
    answer = []
    nums = [i for i in range(1, n+1)]
    while n > 0:
        fact = math.factorial(n-1)
        index = (k-1) // fact
        answer.append(nums[index])
        nums.pop(index)
        k %= fact
        n -= 1
    return answer

"""
우선, math 모듈을 import하여 팩토리얼을 계산할 수 있도록 합니다. 
주어진 n명의 사람을 1부터 n까지의 번호를 가지는 리스트로 초기화합니다. 
그리고 n명 중 k번째 사람을 찾기 위해 반복문을 돌립니다. 각 반복마다, (n-1)!을 계산하여 fact 변수에 저장합니다. 
이를 이용하여 k-1을 fact로 나눈 몫을 인덱스로 하여 nums에서 해당하는 수를 뽑아내고, 이를 answer 리스트에 추가합니다. 
그리고 nums에서 뽑아낸 수를 제거합니다. 
마지막으로 k를 fact로 나눈 나머지를 다시 k에 할당하고, n을 1 감소시킵니다. 
이를 n이 0이 될 때까지 반복합니다. 
마지막으로 answer 리스트를 반환합니다.
"""
