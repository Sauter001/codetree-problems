n, budget = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(n)]
res = 0
for i in range(n):
    price, sail = gifts[i]
    gifts[i] = (price // 2, sail)
    candidates = sorted(map(lambda x: x[0] + x[1], gifts))
    # print(candidates)

    cost = 0
    count = 0
    for c in candidates:
        if cost + c > budget:
            break
        cost += c
        count += 1
    res = max(res, count)

    gifts[i] = (price, sail) # 상태 복구

print(res)