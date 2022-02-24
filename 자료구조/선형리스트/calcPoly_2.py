# 과제 1. 2차원 입력값을 이용하여 다항식 형태를 출력하는 함수(printPoly)와 다항식을 계산하는 함수(calcPoly)를 작성하라.
# 입력 예시: 2
# 출력 예시
# P(x) = +1*7x^3 +1*-4x^2 +0*5x^0 
# X 값-->2
# 40

def printPoly(p_x):
    polyStr = "P(x) = "

    # 코드 작성 부분
    
    for i in range(len(p_x[0])):
        term = p_x[0][i]
        coef = p_x[1][i]
        coef_2 = p_x[2][i]

        if coef >= 0:
            polyStr += '+'
        polyStr += str(coef) + '*' + str(coef_2) + 'x^' + str(term) + ' '
    return polyStr


def calcPoly(xValue, p_x):
    retValue = 0

    # 코드 작성 부분
    for i in range(len(p_x[0])):
        term = p_x[0][i]
        coef = p_x[1][i]
        coef_2 = p_x[2][i]
        retValue += coef * coef_2 * xValue ** term
    return retValue

# 실행 구문 (아래 코드를 수정하지 마시오.)
px = [ [3, 2, 0], [1, 1, 0], [7, -4, 5] ]  # 1행: 차수, 2행: 계수a, 2행: 계수b

pStr = printPoly(px)
print(pStr)

xValue = int(input("X 값-->"))

pxValue = calcPoly(xValue, px)
print(pxValue)