import string
words = list()

with open('words.txt','r') as file:
    line=file.readline().split()
    for word in line:
        if 'c' in word:
            print(word.strip(',.'))