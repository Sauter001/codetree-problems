n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
wifi_range = m * 2 + 1
print(n // wifi_range)