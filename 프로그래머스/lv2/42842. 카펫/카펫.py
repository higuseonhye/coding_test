def solution(brown, yellow):
    for i in range(1, int(yellow**0.5)+1):
        if yellow % i == 0:
            width = yellow // i + 2
            height = i + 2
            if width * height - yellow == brown:
                return [width, height]




