n, butget = map(int, input().split())
presents = [int(input()) for _ in range(n)]

# Please write your code here.
people = 0
for i in range(n):
    discount_presents = [p for p in presents]
    discount_presents[i] //= 2
    discount_presents.sort()
    b = butget
    count = 0
    for p in discount_presents:
        b -= p

        if b < 0:
            break
        count += 1
    people = max(people, count)
        

print(people)