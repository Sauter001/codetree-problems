n = int(input())
arr = list(map(int, input().split()))

def avg(arr):
    return sum(arr) / len(arr)

count = 0
for i in range(n):
    for j in range(i, n):
        sliced = arr[i:j+1]
        count += 1 if avg(sliced) in sliced else 0
print(count)
        