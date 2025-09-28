n = int(input())
digits = []

while n > 1:
    digits.append(str(n % 2))
    n //= 2
digits.append(str(n))
print(''.join(digits[::-1]))
