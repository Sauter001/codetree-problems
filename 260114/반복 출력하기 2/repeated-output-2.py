n = int(input())

def hello(n):
    if n == 0:
        return
    print('HelloWorld')
    hello(n-1)

hello(n)