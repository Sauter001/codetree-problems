A = input()
n = len(A)

# Please write your code here.
cnt = 0
for i in range(n):
    if A[i:i+2] == '((':
        for j in range(i + 2, n):
            if A[j:j+2] == '))':
                cnt += 1
print(cnt)
