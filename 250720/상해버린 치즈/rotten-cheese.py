from collections import defaultdict

N, M, D, S = map(int, input().split())
who_eat = defaultdict(list)
earliest_counter = defaultdict(lambda: 1000) # 사람 p가 치즈 m를 먹은 시간 저장
eater_counter = defaultdict(int)
eater_checker = defaultdict(bool)

for _ in range(D):
    person, cheese, time = map(int, input().split())
    who_eat[(person, time)].append(cheese)

    if time < earliest_counter[(person, cheese)]:
        earliest_counter[(person, cheese)] = time
    if not eater_checker[(person, cheese)]:
        eater_checker[(person, cheese)] = True
        eater_counter[cheese] += 1

sick_p, sick_t = [], []
for _ in range(S):
    person, time = map(int, input().split())
    sick_p.append(person)
    sick_t.append(time)

# 아픈 정보 조회
rotten_cheese_candidates = set(range(1, M + 1))
for p, t in zip(sick_p, sick_t):
    # 아프기 전 먹은 치즈 조회
    eaten_cheeses = { m for m in rotten_cheese_candidates if earliest_counter[(p, m)] < t }
    rotten_cheese_candidates &= eaten_cheeses

result = max(eater_counter[m] for m in rotten_cheese_candidates) if rotten_cheese_candidates else 0
print(result)
 