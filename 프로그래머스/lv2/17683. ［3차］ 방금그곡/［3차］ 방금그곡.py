def solution(m, musicinfos):
    answer = ''
    max_time = 0
    m = change_sound(m)
    for music in musicinfos:
        start, end, title, sound = music.split(',')
        time = (int(end[:2]) - int(start[:2])) * 60 + int(end[3:]) - int(start[3:])
        sound = change_sound(sound)
        full_sound = (sound * (time // len(sound) + 1))[:time]
        if m in full_sound and time > max_time:
            answer = title
            max_time = time
    if not answer:
        answer = "(None)"
    return answer

def change_sound(sound):
    sound = sound.replace('C#', 'c')
    sound = sound.replace('D#', 'd')
    sound = sound.replace('F#', 'f')
    sound = sound.replace('G#', 'g')
    sound = sound.replace('A#', 'a')
    return sound

"""
이 문제는 주어진 멜로디 m이 주어진 여러 개의 노래 중에서 어떤 노래에 포함되어 있는지 찾는 문제
- 각 노래는 시작 시간, 종료 시간, 제목, 멜로디로 이루어진 문자열
- 시작 시간과 종료 시간은 각각 "시:분" 형식

우선 m의 멜로디를 간단하게 만들기 위해 C#, D#, F#, G#, A#를 각각 c, d, f, g, a로 변환
- 각 노래에 대해서 해당 노래의 멜로디를 간단하게 만들고, 노래 길이만큼 멜로디를 반복
- m이 해당 노래의 멜로디에 포함되어 있으면서, 해당 노래가 이전에 찾은 노래들보다 길이가 길다면, 해당 노래를 answer에 저장, 해당 노래의 길이를 max_time에 저장
모든 노래에 대해서 탐색한 뒤, answer가 비어 있으면 "(None)"을 반환
"""
