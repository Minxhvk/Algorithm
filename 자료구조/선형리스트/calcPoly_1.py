# 문제 5. 입력값을 이용하여 다항식 형태를 출력하는 함수(printPoly)와 다항식을 계산하는 함수(calcPoly)를 작성하라.
# 입력 예시: 2
# 출력 예시
# P(x) = +3x^4 -4x^3 +0x^2 +5x^1 +2x^0
# 28

def printPoly(p_x):
    term = len(p_x) - 1	# 최고차항 숫자 = 배열길이-1
    polyStr = "P(x) = "

    for i in range(len(px)):
        coef = p_x[i]	# 계수

        # 코드 작성 구간
        if coef >=0:
            polyStr += '+'
        polyStr += str(coef) + 'x^' + str(term)
        term -= 1

    return polyStr


def calcPoly(xValue, p_x):
    retValue = 0
    term = len(p_x) - 1  # 최고차항 숫자 = 배열길이 - 1

    for i in range(len(px)):
        # 코드 작성 구간
        coef = p_x[i]
        retValue += coef * xValue ** term
        term -= 1
    return retValue


# 실행 구문 (아래 코드를 수정하지 마시오.)
px = [3, -4, 0, 5, 2]			# = +3x^4 -4x^3 +0x^2 +5x^1 +2x^0

pStr = printPoly(px)
print(pStr)

xValue = int(input("X 값-->"))

pxValue = calcPoly(xValue, px)
print(pxValue)