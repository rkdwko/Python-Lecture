keys = input('키를 입력하세요: ').split()
values = map(float, input('값을 입력하세요: ').split())
print(keys)
print(values)

lux = dict(zip(keys, values))
print(lux)