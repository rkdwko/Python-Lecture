numA, numB = map(int, input().split())
a = set(i for i in range(1, numA+1) if numA % i == 0)
b = set(i for i in range(1, numB+1) if numB % i == 0)
# print(a)
# print(b)
divisor = a & b

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)