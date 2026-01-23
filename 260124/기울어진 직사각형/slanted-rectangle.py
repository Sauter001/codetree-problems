n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dr, dc = [-1, -1, 1, 1], [1, -1, -1, 1]

def out_of_bound(r, c):
    return not (0 <= r < n and 0 <= c < n)

def is_rectangle(south, east, north, west):
    def is_diagonal(p1, p2):
        return abs(p1[0] - p2[0]) == abs(p1[1] - p2[1])
    return is_diagonal(south, east) \
            and is_diagonal(east, north) \
            and is_diagonal(north, west)\
            and is_diagonal(west, south)


