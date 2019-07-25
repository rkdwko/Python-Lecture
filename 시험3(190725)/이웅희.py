# 3. 두 개의 정수를 입력받아 작은 수에서부터 큰 수까지(큰 수 포함) 홀수의 합을
# 구해서 출력하는 프로그램을 for loop을 이용하여 작성하시오.

a, b = map(int, input('정수 2개 입력').split())
if a > b:
    a, b = b, a
sum = 0
for i in range(a, b+1):
    if i % 2 ==1:
        sum : 1
print()

# 4. 연 복리 이자율을 입력받아(단위 %) 원금이 2배가 되는데 최소 몇 년이 걸리는지
# 알아보는 프로그램을 while loop을 사용하여 작성하시오.

rate = float(input('이율(%)'))
rate /= 100
year = 1
money = 1
while True:
    money += (1 + rate)
    if money > 2:
        break
    year += 1
print('이율 =', rate*100, '%, 기간 =', year, '년')

# 5. bts 리스트가 주어졌을 때 아래와 같은 답이 나오도록 print문을 작성하시오.
# bts = ['RM', '진', '슈가', '제이홉', '지민', '뷔', '정국']
# 1) 뷔
print(bts[-2])

# 2) ['RM']
print(bts[0:1])

# 3) ['뷔', '정국']
print(bts[-2:])

# 4) ['슈가', '제이홉', '지민']
print(bts[2:5])

# 5) ['RM', '슈가', '지민', '정국']
print(bts[::2])

# 6. 다음과 같은 딕셔너리 VEGETABLES가 주어졌을 때 아래 그림과 같이
# 가격이 높은 것부터 내림차순으로 출력하는 프로그램을 작성하되,
# 가격은 길이를 7로 만들고 1000단위 ,를 찍은 뒤 우측정렬 하시오.
# vegetables = {'가지':800, '오이':600, '수박':15000, '호박':1000, '깻잎':500}
# 수박: 15,000
# 호박: 1,000
# 가지: 800
# 오이: 600
# 갯잎: 500

vegetables = {'가지':800, '오이':600, '수박':15000, '호박':1000, '깻잎':500}

import operator
sv = sorted(a.items(), key=operator.itemgetter(1), reverse=True)
for veg, price in sv:
    print('$s:$7s' % (veg, format(price, ',')))

# 7. 앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고
# 부른다. 두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 X 99) 이다.
# 세 자리 수 X, Y(단, x <= y)를 곱해 만들 수 있는 가장 큰 대칭수는 얼마이고
# 그때 x, y의 값을 얼마인가?

def isPalindrome(a):
    for i in range(len(a)//2):
        if a[i] != a[-1-i]:
            return False
    return True

maxNum = 0
for i in range(100, 1000):
    for k in range(100, 1000):
        if isPalindrome(str(i*k)):
            if i*k > maxNum:
                maxNum = i*k
print(maxNum)

# 8. 다음의 규칙대로 동작하는 프로그램을 작성하시오.
# 타일판은 5 x 5
# 타일 종류는 1~4의 네가지 랜덤값으로 정한 후 타일판 출력
# 가로나 세로로 3개 이상 같은 타일이 연속될 경우 타일을 '*'로 바꾸고 타일판 출력



# 9. 다음과 같은 리스트 a가 주어졌을 때 a의 각 원소를 제곱한 값을 원소로 갖는
# 리스트 b를 람다표현식을 사용하여 구하시오.
# a = [1, 3, 5, 7, 9])