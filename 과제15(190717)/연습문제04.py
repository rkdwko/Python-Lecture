# 4. 세 자연수 a, b, c가 피타고라서 정리 a^ + b^ = c^를 만족하는 피타고라스 수라고 부른다.
# (여기서 a < b < c 이고 a + b > c)
# 예를들면, 3^ + 4^ = 9 + 16 = 25 = 5^dlamfh 3, 4, 5는 피타고라서 수입니다.
# a + b + c = 1000 인 피타고라스 수를 구하시오.(답은 한가지 뿐이다.)

outerBreak = False
for a in range(1, 333):
    if outerBreak:
        break
    for b in range(a+1, 500):
        c = 1000 - a - b
        if c < b:
            continue
        if a**2 + b**2 == c**2:
            print(a, b, c, a+b+c)
            print(a**2, b**2, c**2)
            outerBreak = True
            break;