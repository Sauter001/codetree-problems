n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
sequence_counts = []
cnt = 0

for i in range(n):
    if i == 0:
        cnt += 1
    elif arr[i] != arr[i - 1]:
        sequence_counts.append(cnt)
        cnt = 1
    else:
        cnt += 1

if not sequence_counts:
    sequence_counts.append(cnt)
print(max(sequence_counts))