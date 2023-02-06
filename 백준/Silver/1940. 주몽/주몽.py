n = int(input().strip())
m = int(input().strip())
a = [int(i) for i in input().strip().split()]

cnt = 0
for i in a:
    if m-i in a:
        cnt += 1

print(cnt//2)
