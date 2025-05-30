from itertools import combinations

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
xs, ys = set(p[0] for p in points), set(p[1] for p in points)
positions = [(x, 'x') for x in xs] + [(y, 'y') for y in ys]

def is_covered(p, lines):
    for line in lines:
        match line:
            case (x, 'x'):
                if p[0] == x: return True
            case (y, 'y'):
                if p[1] == y: return True

    return False

for c in combinations(positions, 3):
    if all(is_covered(p, c) for p in points):
        print(1)
        break
else:
    print(0)
                