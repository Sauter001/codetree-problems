from sortedcontainers import SortedDict

sorted_dict = SortedDict()
n = int(input())

def add(k, v):
    sorted_dict[k] = v

def remove(k):
    sorted_dict.pop(k, 'None')

def find(k):
    if k in sorted_dict:
        return int(sorted_dict[k])
    else:
        return -1

def print_list():
    if not sorted_dict:
        print('None')
        return
    print(*[v for k, v in sorted_dict.items()])

for _ in range(n):
    command = input().split()
    op = command[0]
    if op == 'add':
        add(command[1], command[2])
    elif op == 'remove':
        remove(command[1])
    elif op == 'find':
        val = find(command[1])
        print(val if val > 0 else 'None')
    elif op == 'print_list':
        print_list()
