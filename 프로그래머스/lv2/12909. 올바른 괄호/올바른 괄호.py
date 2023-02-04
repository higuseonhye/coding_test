"""
괄호가 제대로 짝지어졌는지 확인하는 함수입니다.
입력받은 문자열을 기준으로 괄호가 제대로 짝지어졌는지 확인하기 위해서 stack 리스트를 생성합니다. 
괄호가 열리면 stack에 추가, 닫히면 stack에서 꺼내는 방식으로 괄호의 짝을 확인합니다. 
최종적으로 stack이 비어있으면 True, 아니면 False를 리턴합니다.
"""
def solution(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack
"""
stack: https://www.geeksforgeeks.org/stack-in-python/
- A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner.
"""
