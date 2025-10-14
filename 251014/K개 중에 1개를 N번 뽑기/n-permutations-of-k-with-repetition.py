import sys

k, n = map(int, input().split())

def perm(k, n, arr):
    if n == 0:
        print(*arr)
        return
    
    for i in range(1, k + 1):
        arr.append(i)
        perm(k, n - 1, arr)
        arr.pop()

perm(k, n, [])