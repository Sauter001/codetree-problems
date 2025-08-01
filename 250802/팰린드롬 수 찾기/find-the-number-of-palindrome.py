X, Y = map(int, input().split())

def is_palin(s: str):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

count = 0
for x in range(X, Y + 1):
    count += 1 if is_palin(str(x)) else 0
print(count)