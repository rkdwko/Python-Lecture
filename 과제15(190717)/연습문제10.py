# 1부터 10까지 자연수를 각각 제곱해 더하면 다음과 같다.(제곱의 합)
# 1^+2^+...+^10^ = 385
# 1부터 10을 먼저 더한 다음에 그 결과를 제곱하면 다음과 같습니다.(합의 제곱)
# (1+2+...+10)^ = 55^ = 3025
# 따라서 1부터 10까지 자연수에 대해 "합의 제곱"과 제곱의 합"의 차이는 3025 - 385 = 2640이 된다.
# 입력으로 자연수 N을 받아, 1부터 N까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이는 얼마인가?

n = int(input('자연수 입력> '))

sumOfSquare = 0
sum = 0
for i in range(1, n+1):
    sum += i
    sumOfSquare += i ** 2
squareOfSum = sum ** 2
print('합의 제곱 =', squareOfSum)
print('제곱의 합 =', sumOfSquare)
print('차이 =', squareOfSum - sumOfSquare)