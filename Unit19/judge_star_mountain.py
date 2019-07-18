height = int(input())
for i in range(1, height+1):
    for k in range(height-i):
        print(' ', end='')
    for k in range(i*2-1):
        print('*', end='')
    print()