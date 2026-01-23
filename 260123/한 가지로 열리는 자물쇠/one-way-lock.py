N = int(input())
lock = tuple(map(int, input().split()))
opened = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            key = (i, j, k)
            unlock = False
            for digit in range(3):
                if abs(key[digit] - lock[digit]) <= 2:
                    unlock = True
                    break
            opened += 1 if unlock else 0

print(opened)