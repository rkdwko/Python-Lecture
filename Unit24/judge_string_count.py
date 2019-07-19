paragraph = input().split()
count = 0
for words in paragraph:
    words.strip(',.')
    if words == 'the':
        count+ = 1
    print(count)