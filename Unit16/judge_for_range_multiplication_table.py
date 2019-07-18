n = int(input())

if 2 <= n <= 9:
    for i in range(1, 10):
        print(n, '*', i, '=', n*i)