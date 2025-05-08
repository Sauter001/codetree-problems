import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.
def bin_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

for q in queries:
    print(bin_search(arr, q))