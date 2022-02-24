# 문제 9. 노드 삭제 함수를 추가하고 입력값을 이용하여 단순 연결 리스트를 생성하라.
# 출력 예시
# ## 초기 연결 리스트 ##
# R 파이썬 C C++ JAVA MATLAB
# ## R 삭제 결과 ##
# 파이썬 C C++ JAVA MATLAB
# ## C++ 삭제 결과 ##
# 파이썬 C JAVA MATLAB
# ## MATLAB 삭제 결과 ##
# 파이썬 C JAVA

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


def deleteNode(deleteData):
    global memory, head, current, pre

    # 코드 작성 구간
    if head.data == deleteData:
        current = head
        head = head.link
        del current
    else:
        current = head
        while current.link != None:
            pre = current
            current = current.link
            if current.data == deleteData:
                pre.link = current.link
                del current
                break

# 실행 구문 (아래 코드를 수정하지 마시오.)
memory = []
head, current, pre = None, None, None
dataArray = ['R', '파이썬', 'C', 'C++', 'JAVA', 'MATLAB']

node = Node()			# 첫 번째 노드
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:] :		# 두 번째 노드부터
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

print('## 초기 연결 리스트 ##')
printNodes(head)

print('\n## R 삭제 결과 ##')
deleteNode("R")
printNodes(head)

print('\n## C++ 삭제 결과 ##')
deleteNode("C++")
printNodes(head)

print('\n## MATLAB 삭제 결과 ##')
deleteNode("MATLAB")
printNodes(head)