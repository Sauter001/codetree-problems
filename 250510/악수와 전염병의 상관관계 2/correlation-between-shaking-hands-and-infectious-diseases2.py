N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.
infected_list = [False] * (N + 1)
infected_list[P] = True
infected_times = [-1] * (N + 1)
infected_times[P] = 0
handshake_counts = [0] * (N + 1)
handshakes.sort()

# 감염시키는 사람은 전염됐다고 가정
def infect_person(infected_time, from_dev, to_dev):
    if handshake_counts[from_dev] < K:
        if not infected_list[to_dev]:
            infected_list[to_dev] = True
            infected_times[to_dev] = infected_time
    handshake_counts[from_dev] += 1     

for t, x, y in handshakes:
    # print(t,x,y)
    for a, b in [(x, y), (y, x)]:
        if infected_list[a] and infected_times[a] < t:
            infect_person(t, a, b)
    # print(handshake_counts[1:])

print(''.join('1' if infected else '0' for infected in infected_list[1:]))