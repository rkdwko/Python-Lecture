files = input().split()
print('{0}'.format(list(map(lambda x: x.split('.')[0], files))))