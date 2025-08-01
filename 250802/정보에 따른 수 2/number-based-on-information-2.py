T, a, b = map(int, input().split())
chars, positions = [], []
for _ in range(T):
    char, pos = input().split()
    chars.append(char)
    positions.append(int(pos))

count = 0
for i in range(a, b + 1):
    d1, d2 = 1000, 1000
    
    for c, p in zip(chars, positions):
        if c == 'S':
            d1 = min(d1, abs(i - p))
        elif c == 'N':
            d2 = min(d2, abs(i - p))
    if d1 <= d2:
        count += 1
print(count)