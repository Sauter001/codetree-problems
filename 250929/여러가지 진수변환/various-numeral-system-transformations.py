N, B = map(int, input().split())
digits = []

while N >= B:
    digits.append(N % B)
    N //= B
digits.append(N)
print(digits[::-1], sep='')
