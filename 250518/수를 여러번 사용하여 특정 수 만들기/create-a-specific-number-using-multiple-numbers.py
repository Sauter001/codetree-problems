A, B, C = map(int, input().split())

# Please write your code here.
max_val = 0
for i in range(C // A + 1):
    x = (C - A * i) // B
    val = A*i + B*x
    max_val = max(max_val, val)

print(max_val)
    