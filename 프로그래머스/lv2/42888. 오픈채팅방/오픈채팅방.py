from collections import defaultdict, deque

def solution(record):
    uid_dict = defaultdict(str)
    q = deque()
    answer = []
    for rec in record:
        split_record = rec.split(' ')
        if split_record[0] == 'Enter':
            uid_dict[split_record[1]] = split_record[2]
            q.append([split_record[1], '님이 들어왔습니다.'])
        elif split_record[0] == 'Leave':
            q.append([split_record[1], '님이 나갔습니다.'])
        elif split_record[0] == 'Change':
            uid_dict[split_record[1]] = split_record[2]
    
    for uid, event in q:
        answer.append(uid_dict[uid]+event)
    return answer

"""
이 Python3 코드는 "Enter", "Leave", "Change" 이벤트를 녹음하고 이벤트 기록을 반환하는 프로그램입니다.

- collections 모듈에서 defaultdict와 deque를 가져옵니다.
- "solution" 함수는 입력으로 "record" 리스트를 받습니다.
- "uid_dict" defaultdict 딕셔너리는 사용자 ID를 키로하고 이름을 값으로 가집니다.
- "q" deque는 사용자의 "Enter" 또는 "Leave" 이벤트를 기록합니다.
- "answer" 리스트는 결과를 기록합니다.
- "record" 리스트에서 각 레코드를 "rec"에 가져옵니다. 각 레코드는 공백으로 구분되어 있으며, "split_record" 리스트에 저장됩니다.
- "split_record"의 첫 번째 원소가 "Enter"인 경우 "uid_dict" 딕셔너리에 사용자 ID를 키로하고 이름을 값으로 저장합니다. 
    또한, "q" deque에 "[사용자 ID, '님이 들어왔습니다.']"를 추가합니다.
- "split_record"의 첫 번째 원소가 "Leave"인 경우 "q" deque에 "[사용자 ID, '님이 나갔습니다.']"를 추가합니다.
"""

"""
이 Python3 코드는 어떤 사용자의 액션 기록을 관리하는 프로그램입니다.
- from collections import defaultdict, deque부분에서 defaultdict와 deque 모듈을 import 합니다. 
- defaultdict는 기본 값을 가진 딕셔너리 객체를 생성할 수 있는 클래스입니다. deque는 양쪽에서 삽입과 삭제가 가능한 컨테이너입니다.
- solution 함수는 record 리스트를 매개변수로 받습니다. uid_dict 딕셔너리는 각 사용자의 아이디와 닉네임을 매칭하여 저장합니다. 
    q 덱은 사용자의 액션 기록을 저장합니다. 
    answer 리스트는 결과를 저장할 공간입니다.
- for rec in record: 부분에서 record 리스트에서 각 사용자의 액션을 처리합니다. 
    split_record 리스트는 각 액션 기록을 스페이스바를 기준으로 나눈 것입니다.
"""
