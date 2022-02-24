# 과제 1. 그래프 순회를 이용하여 허니버터칩 최대 보유 편의점(개수) 출력하라.
# (강의자료 응용예제 01 참고)
# 출력 예시
# ## 편의점 그래프 ##
# 0	1	1	0	0	
# 1	0	1	1	0	
# 1	1	0	1	0	
# 0	1	1	0	1	
# 0	0	0	1	0	

# ## 허니버터칩 최대 보유 편의점(개수)
# 편의점: MiniStop, 보유 개수: 90개

class Graph():
    def __init__ (self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(g):
    # 코드 작성 구간: 그래프 출력 (print 함수 사용시 end='\t')
    print()
    for row in range(g.SIZE):
      for col in range(g.SIZE):
        print(g.graph[row][col], end = '\t')
      print()
    print()    

def find_max_count(g, storeAry):
    stack = []  # 스택 초기화
    visitedAry = []  # 방문한 정점 초기화
    current = 0  # 시작 정점
    stack.append(current)
    visitedAry.append(current)
    # 코드 작성 구간: 그래프 순회 이용하여 최대 보유 편의점, 개수 반환
    maxSore = current
    maxCount = storeAry[current][1]
    stack.append(current)
    visitedAry.append(current)

    while(len(stack) != 0):
      next = None
      for vertex in range(g.SIZE):
        if g.graph[current][vertex] == 1:
          if vertex not in visitedAry :
            next = vertex
            break

      if next != None :
        current = next
        stack.append(current)
        visitedAry.append(current)
        if storeAry[current][1] > maxCount :
          maxStore = storeAry[current][0]
          maxCount = storeAry[current][1]
      else:
        current = stack.pop()
      
    return maxStore, maxCount
      


# 실행 구문 (아래 코드를 수정하지 마시오.)
storeAry = [['GS25', 30], ['CU', 60], ['Seven11', 10], ['MiniStop', 90], ['Emart24', 40]]  # 편의점 배열
GS25, CU, Seven11, MiniStop, Emart24 = 0, 1, 2, 3, 4  # 편의점명, 숫자 매핑

G1 = Graph(5)  # 빈 그래프 생성
G1.graph[GS25][CU] = 1; G1.graph[GS25][Seven11] = 1
G1.graph[CU][GS25] = 1; G1.graph[CU][Seven11] = 1; G1.graph[CU][MiniStop] = 1
G1.graph[Seven11][GS25] = 1; G1.graph[Seven11][CU] = 1; G1.graph[Seven11][MiniStop] = 1
G1.graph[MiniStop][Seven11] = 1; G1.graph[MiniStop][CU] = 1; G1.graph[MiniStop][Emart24] = 1
G1.graph[Emart24][MiniStop] = 1

print('## 편의점 그래프 ##')
print_graph(G1)  # 그래프 출력

print(f'## 허니버터칩 최대 보유 편의점(개수)')
maxStore, maxCount = find_max_count(G1, storeAry)  # 최대 보유 편의점 찾기
print(f'편의점: {maxStore}, 보유 개수: {maxCount}개')