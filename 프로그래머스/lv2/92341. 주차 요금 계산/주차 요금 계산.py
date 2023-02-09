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
