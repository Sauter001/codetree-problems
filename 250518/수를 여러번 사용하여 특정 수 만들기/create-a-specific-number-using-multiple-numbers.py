A, B, C = map(int, input().split())

# Please write your code here.
factors = [0, 0]

def max_value(factors):
    val = factors[0] * A + factors[1] * B

    if val > C:
        return -1
    else:
        return max(val, max_value([factors[0] + 1, factors[1]]), max_value([factors[0], factors[1] + 1]))

print(max_value(factors))
    