words = list()
with open('words2.txt', 'r') as file:
    for word in file:
        temp = word.strip('\n')
        words.append(temp)
for word in words:
    if word == word[::-1]:
        print(word)