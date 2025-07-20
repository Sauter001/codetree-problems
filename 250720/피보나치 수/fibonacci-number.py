n = int(input())
memo = [-1] * (n + 1)
memo[0] = 0
memo[1] = 1

def f(n):
    if memo[n] < 0:
        memo[n] = f(n - 1) + f(n - 2)
    return memo[n]
print(f(n))