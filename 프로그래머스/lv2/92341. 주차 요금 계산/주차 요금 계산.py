from collections import defaultdict

def solution(fees, records):
    answer = []
    dict = defaultdict(int)
    total = defaultdict(int)
    out = 23*60 + 59

    for record in records:
        times, number, c = record.split()
        hours, minutes = map(int, times.split(":"))
        time = hours*60 + minutes

        if number in dict:
            total[number] += time - dict[number]
            del dict[number]
        else:
            dict[number] = time

    for key, value in dict.items():
        total[key] += out - value

    for key, value in total.items():
        fee = fees[1] if value <= fees[0] else (value - fees[0] + fees[2] - 1) // fees[2] * fees[3] + fees[1]
        answer.append((key, fee))

    answer.sort()
    return [value[1] for value in answer]

"""
solution 함수에서 통화 기록과 통화요금 정책을 받아 각 전화번호의 통화비용을 계산하여 정렬한 후 반환합니다.

defaultdict는 파이썬의 딕셔너리 구현에서 기본 값을 설정하여 사용할 수 있는 딕셔너리 클래스입니다.

dict와 total 변수는 각 전화번호에 대한 전화의 시작 시간과 각 전화번호에 대한 총 통화시간을 저장합니다.

out 변수는 하루가 끝나는 시간을 분 단위로 표현한 값입니다.

for record in records 루프는 records 리스트에 있는 통화 기록을 하나씩 꺼내어 처리합니다.

루프 내에서 통화 기록을 시간, 번호, 통화 상태 (수신, 발신) 으로 분리합니다. 
"""
