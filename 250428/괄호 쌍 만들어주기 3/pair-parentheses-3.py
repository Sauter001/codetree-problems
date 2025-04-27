A = input()
N = len(A)

# Please write your code here.
cnt = 0
for i, t in enumerate(A):
    if t == '(':
        for j in range(i + 1, N):
            if A[j] == ')':
                cnt += 1

print(cnt)