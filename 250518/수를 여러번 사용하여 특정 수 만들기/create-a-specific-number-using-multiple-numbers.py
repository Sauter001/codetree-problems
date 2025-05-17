A, B, C = map(int, input().split())

# Please write your code here.
factors = [0, 0]

def max_value(factors):
    val = factors[0] * A + factors[1] * B

    if val > C:
        return -1
    else:
        a, b = factors
        return max(val, max_value([a + 1, b]), max_value([a, b + 1], max_value([a + 1, b + 1])))

print(max_value(factors))
    