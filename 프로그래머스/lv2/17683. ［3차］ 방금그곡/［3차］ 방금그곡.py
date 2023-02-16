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
