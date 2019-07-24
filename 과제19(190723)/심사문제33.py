def countdown(n):
    i = n
    def continueCount():
        nonlocal
        i
        r = i
        i -= 1
        return r
    return continueCount

n = int(input())

c = countdown(n)
for i in range(n):
    print(c(), end=' ')