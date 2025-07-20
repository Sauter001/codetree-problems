X, Y = map(int, input().split())

# Please write your code here.
def convert_to_digits(n):
    res = []
    divisor = 10
    while n > 0:
        res.append(n % divisor)
        n //= divisor
    return res

count = 0
for x in range(X, Y+1):
    digits = convert_to_digits(x)
    digit_counter = {}
    for d in digits:
        if d not in digit_counter:
            digit_counter[d] = 0
        digit_counter[d] += 1
    
    one_count = 0
    for v in digit_counter.values():
        if v == 1: one_count += 1
    
    if one_count == 1:
        count += 1
print(count)