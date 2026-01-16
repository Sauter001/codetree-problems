word1 = input()
word2 = input()

def join(s):
    return ''.join(s)

sorted_word1 = sorted(list(word1))
sorted_word2=  sorted(list(word2))
print('Yes' if join(sorted_word1) == join(sorted_word2) else 'No')


