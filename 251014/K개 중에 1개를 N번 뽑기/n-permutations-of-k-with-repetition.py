k, n = map(int, input().split())

def perm(k, n, arr):
    if n == 0:
        print(*arr)
    
    for i in range(1, k + 1):
        if i in arr: 
            continue

        arr.append(i)
        perm(k, n - 1)
        arr.pop()

perm(k, n, [])