# 4. 텍스트를 파일에서 읽어 단어의 개수를 세는 프로그램 Word Count를 작성하시오.
# 입력은 텍스트 파일이고, 구분자는 마침표(','), 쉼표(','), 공백(',')이다.
# 출력은 총 단어수와 가장 많이 나온순서대로 단어 10개와 그 단어의 빈도이다.

filename = input('파일 이름> ')
wordsDict = dict()

with open(filename, 'r') as file:
    for line in file:
        linewords = line.replace('(', ' ').replace(')', ' ').replace(',', ' ').replace('.', ' ').split()
        #print(linewords)
        for word in linewords:
            count = wordsDict.get(word, 0)
            #print(count, end=' ')
            if count == 0:
                wordsDict.setdefault(word, 1)
            else:
                wordsDict.update(dict([(word, count+1)]))

import operator
wordsList = sorted(wordsDict.items(), key=operator.itemgetter(1), reverse=True)
for i in range(15):
    print(wordsList[i])