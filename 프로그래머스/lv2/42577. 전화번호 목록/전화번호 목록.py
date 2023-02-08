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



