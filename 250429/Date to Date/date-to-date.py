m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if m1 == m2:
    print(d2 - d1 + 1)
else:
    days = (num_of_days[m1] - d1 + 1) + d2
    for d in range(m1 + 1, m2):
        days += num_of_days[d]
    print(days)