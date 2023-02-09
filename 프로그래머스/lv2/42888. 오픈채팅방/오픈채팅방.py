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
