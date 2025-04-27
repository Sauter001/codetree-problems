import sys
input = sys.stdin.readline

A = input()
N = len(A)

# Please write your code here.
cnt = 0
open_cnt = 0
for t in A:
    if t == '(':
        open_cnt += 1
    elif t == ')':
        cnt += open_cnt

print(cnt)