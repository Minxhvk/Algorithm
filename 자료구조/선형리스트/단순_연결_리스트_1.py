# 과제 2. 입력값을 이용하여 단순 연결 리스트를 생성하고 출력하라.
# 입력 예시
# dataArray = ["파이썬", "C", "C++", "JAVA", "MATLAB"]
# 출력 예시
# >> printNodes(head)
# 1: 파이썬, 2: C, 3: C++, 4: JAVA, 5: MATLAB,

class Node():
	def __init__ (self):
		self.data = None
		self.link = None

def printNodes(start):
    # 코드 작성 부분  
    current = start
    if current == None:
        return
    
    print(memory.index(current)+1, ':', current.data, end='  ')
    
    while current.link != None:
        current = current.link
        print(memory.index(current)+1, ':',current.data, end='  ')


# 실행 구문 (아래 코드를 수정하지 마시오.)
memory = []
head, current, pre = None, None, None
dataArray = ["파이썬", "C", "C++", "JAVA", "MATLAB"]

node = Node()		# 첫 번째 노드
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:]:	# 두 번째 이후 노드
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNodes(head)