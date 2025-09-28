binary = input()
res = 0
digit = 0

for d in binary[::-1]:
    num = int(d)
    res += 2 ** digit * num
    digit += 1
print(res)
