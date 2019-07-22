# 5. 다음의 지시대로 폴더와 파일을 프로그램에서 만드시오.
# 5-1. 랜덤으로 1, 2, 3 중 하나를 내용으로 갖는 txt 파일 100개를 하나의 디렉토리(c:/Temp/Ex04)안에 생성하는
# 코드를 작성하시오.(파일 제목은 4자리 정수를 랜덤으로 할당. ex - 1382.txt, 0201.txt, 9012.txt, ...)
# 5-2. 제목이 0000~3333인 txt파일은 low 폴더로, 3334~6666인 txt 파일은 mid 폴더로, 6667~9999인 파일은
# high폴더로 이동시키는 코드를 작성하시오.
# 5-3. low, mid, high 폴더 안에 제목이 1, 2, 3인 폴더를 각각 만들고, txt 파일 안의 내용에 따라
# txt파일을 폴더안으로 이동시켜 분류하시오.
# 5-4. 결론적으로 c:/Temp/Ex04 폴더 밑에는 low, mid, high 폴더가 3개가 생기고, 이 각각의 폴더에는
# 1, 2, 3 폴더가 각각 생기고 이 폴더밑에 파일이 들어 있어야 함.

import os
import random as rd
PATH = 'c:/Temp/Ex04'
os.mkdir(PATH)
os.chdir(PATH)
for dirname in ('low', 'mid', 'high'):
    os.mkdir(PATH + '/' + dirname)
    for num in ('1', '2', '3'):
        os.mkdir(PATH + '/' + dirname + '/' + num)

for i in range(100):
    filenumber = rd.randint(0, 9999)
    content = str(rd.randint(1, 3))
    if filenumber <= 3333:
        dirname = 'low'
    elif filenumber <= 6666:
        dirname = 'mid'
    else:
        dirname = 'high'
    filename = dirname + '/' + content + '/' + '%04d.txt' % filenumber
    file = open(filename, 'w')
    file.write(content)
    file.close()