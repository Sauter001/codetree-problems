a = input()
binary_digits = [int(x) for x in a]

# Please write your code here.
def bin_to_digit(binary_digits):
    digit = 0
    res = 0
    for d in binary_digits[::-1]:
        res += 2**(digit) * d
        digit += 1
    return res

# print(binary_digits)
if all(binary_digits):
    binary_digits[-1] = 0
else:
    for i in range(len(binary_digits)):
        if binary_digits[i] == 0:
            binary_digits[i] = 1
            break
print(bin_to_digit(binary_digits))

