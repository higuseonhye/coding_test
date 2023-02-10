from itertools import product
def solution(word):
    answer = 0
    
    total_dict = []
    for i in range(1, 6):
        dictionary = list(map("".join, product(['A','E','I','O','U'], repeat = i)))
        total_dict.extend(dictionary)
    
    total_dict.sort()
    for i in range(len(total_dict)):
        if total_dict[i] == word:
            answer = i+1
    return answer

"""
주어진 단어(word)의 순서를 알아내는 프로그램입니다.

- 코드의 첫 부분에서 "itertools" 라이브러리에서 "product" 함수를 가져옵니다. 이 함수는 "repeat" 횟수만큼 "A","E","I","O","U" 문자를 조합한 모든 문자열을 만듭니다.
- 함수 solution(word)가 시작되면, "answer" 변수를 0으로 초기화합니다.
- "total_dict" 리스트를 생성합니다. 이 리스트는 1~5 길이의 모음만으로 구성된 문자열의 리스트를 포함합니다.
- "total_dict" 리스트에 "dictionary" 리스트를 확장하면서, 1~5 길이의 모음만으로 구성된 모든 문자열을 "total_dict"에 추가합니다.
- "total_dict" 리스트를 정렬합니다.
- "total_dict" 리스트의 각 원소와 "word"를 비교하여 같으면, "answer" 변수에 해당 인덱스 + 1을 할당합니다.
- "answer" 값을 반환합니다.
"""
