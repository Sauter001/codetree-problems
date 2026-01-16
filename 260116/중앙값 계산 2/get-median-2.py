n = int(input())
arr = list(map(int, input().split()))

def medium(arr):
    arr = sorted(arr)
    mid = len(arr) // 2
    if len(arr) % 2 == 0:
        return (arr[mid] + arr[mid - 1]) // 2
    else:
        return arr[mid]

for i in range(n):
    if i % 2 == 0:
        sliced = arr[:i+1]
        print(medium(sliced), end=' ')    