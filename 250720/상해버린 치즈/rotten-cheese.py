from collections import defaultdict

N, M, D, S = map(int, input().split())
who_eat = defaultdict(list)
earliest_counter = defaultdict(list) # 사람 p가 치즈를 먹은 시간들 저장

for _ in range(D):
    person, cheese, time = map(int, input().split())
    who_eat[(person, time)].append(cheese)
    earliest_counter[person].append(time)

# 시간 정렬
for ct in earliest_counter.values():
    ct.sort()

sick_p, sick_t = [], []
for _ in range(S):
    person, time = map(int, input().split())
    sick_p.append(person)
    sick_t.append(time)

# 아픈 정보 조회
rotten_cheese_candidates = set()
for p, t in zip(sick_p, sick_t):
    # 아프기 전 먹은 치즈 조회
    for i in range(earliest_counter[p][0], t):
        # print(f"{p}, {t}: {i} => {who_eat[(p, i)]}")
        rotten_cheese_candidates &= set(who_eat[(p, i)])

checker = [False] * (N + 1)
for (p, t), cheeses in who_eat.items():
    # print(f"{p}, {t}: {cheeses}")
    for c in cheeses:
        if c in rotten_cheese_candidates and not checker[p]:
            checker[p] = True

print(sum(checker))
 