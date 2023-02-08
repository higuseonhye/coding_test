def solution(phone_book):
    phone_book.sort()
    for i, num1 in enumerate(phone_book):
        for j in range(i + 1, len(phone_book)):
            num2 = phone_book[j]
            if num2.startswith(num1):
                return False
            if num1[:len(num2)] != num2:
                break
    return True

"""
이 코드는 주어진 phone_book 리스트에서, 어떤 번호의 접두사가 다른 번호인지 확인하는 것입니다.

우선, phone_book 리스트를 정렬합니다. 그런 다음, 리스트에서 모든 번호를 순서대로 확인합니다. 
각 번호에 대해, 나중에 나오는 번호 중 첫 번째 번호부터 확인하여, 어떤 번호가 현재 번호의 접두사인지 확인합니다. 
만약 그렇다면, False를 반환합니다. 
만약 현재 번호의 접두사가 아닌 것이 발견되면, 나머지 번호를 확인할 필요 없이 반복문을 빠져나갑니다.

만약 모든 번호를 확인한 후, 아무런 접두사가 발견되지 않았다면, True를 반환합니다.
"""
