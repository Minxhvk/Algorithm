# 문제 8. 노드 삽입 함수를 추가하고 입력값을 이용하여 단순 연결 리스트를 생성하라.
# 출력 예시
# ## 초기 연결 리스트 ##
# 파이썬 C++ MATLAB
# ## C++ 위치에 C 추가 결과 ##
# 파이썬 C C++ MATLAB
# ## MATLAB 위치에 JAVA 추가 결과 ##
# 파이썬 C C++ JAVA MATLAB

class Node():
	def __init__ (self):
		self.data = None
		self.link = None

def printNodes(start):
    # 코드 작성 구간
    current = start
    if current == None:
        return
    
    print(current.data, end=' ')
    
    while current.link != None:
        current = current.link
        print(current.data, end=' ')

def insertNode(findData, insertData):
    global memory, head, current, pre

    # 코드 작성 부분(첫 번째 노드 삽입)
    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
    # 코드 작성 부분(중간 노드 삽입)
    else:
        current = head
        find_flag = False
        while current.link != None:
            pre = current
            current = current.link
            if current.data == findData:
                node = Node()
                node.data = insertData
                node.link = current
                pre.link = node
                find_flag = True
                break

    # 코드 작성 부분(마지막 노드 삽입)
        if not find_flag:
            node = Node()
            node.data = insert_data
            current.link = node

# 실행 구문 (아래 코드를 수정하지 마시오.)
memory = []
head, current, pre = None, None, None
dataArray = ["파이썬", "C++", "MATLAB"]

node = Node()			# 첫 번째 노드
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:]:		# 두 번째 노드부터
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

print('## 초기 연결 리스트 ##')
printNodes(head)

print('\n## 파이썬 위치에 R 추가 결과(첫번째 노드 삽입) ##')
insertNode("파이썬", "R")
printNodes(head)

print('\n## C++ 위치에 C 추가 결과(중간 노드 삽입) ##')
insertNode("C++", "C")
printNodes(head)

print('\n## MATLAB 위치에 JAVA 추가 결과(마지막 노드 삽입) ##')
insertNode("MATLAB", "JAVA")
printNodes(head)