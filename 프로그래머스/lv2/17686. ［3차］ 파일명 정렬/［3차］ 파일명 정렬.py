import re

def solution(files):
    answer = []
    
    head_num_tail = [re.split(r"([0-9]+)", file) for file in files]    
    sorted_head_num_tail = sorted(head_num_tail, key=lambda x: (x[0].lower(), int(x[1])))
    answer = ["".join(h_n_t) for h_n_t in sorted_head_num_tail]
    
    return answer

"""
위의 코드는 파일 이름을 정렬하는 프로그램입니다.

- files는 파일 이름의 리스트입니다.
- re.split() 함수를 사용하여 파일 이름을 head_num_tail 리스트에 분리합니다. 
    re.split()은 파일 이름을 r"([0-9]+)"와 매칭되는 정규 표현식과 분리하여 각 부분을 요소로 갖는 리스트를 반환합니다.
- sorted() 함수를 사용하여 head_num_tail 리스트를 정렬합니다. 
    key 인수로 사용된 lambda 함수는 x 리스트의 첫 번째 요소를 소문자로 변환하여 비교하고, 
    두 번째 요소는 int() 함수를 사용하여 정수로 변환하여 비교합니다.
- "".join() 함수를 사용하여 head_num_tail 리스트의 요소를 결합하여 answer 리스트를 만듭니다.
- answer 리스트를 반환합니다
"""
