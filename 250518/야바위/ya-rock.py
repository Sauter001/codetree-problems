n = int(input())
moves = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n)]
s1, s2, o = zip(*moves)
swap1, swap2, opens = list(s1), list(s2), list(o)

# Please write your code here.
def do_yabawi(cups, s1, s2, cup_to_open):
    cups[s1], cups[s2] = cups[s2], cups[s1]
    return cups[cup_to_open]

max_score = 0
for i in range(3):
    cups = [0] * 3
    cups[i] = 1

    score = 0
    for j in range(n):
        score += do_yabawi(cups, swap1[i], swap2[i], opens[i])

    max_score = max(max_score, score)
print(max_score)