N = int(input())

def s(acc, n):
    if n <= 1:
        return acc + 1
    return s(acc + n, n - 1)
print(s(0, N))
