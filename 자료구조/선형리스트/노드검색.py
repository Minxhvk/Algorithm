# 문제 10. 노드 검색 함수를 추가하고 단순 연결 리스트에서 노드를 검색하라.
# 출력 예시
# ## 초기 연결 리스트 ##
# R 파이썬 C C++ JAVA MATLAB
# ## R 검색 결과 ##
# R
# ## C++ 검색 결과 ##
# C++
# ## MATLAB 검색 결과 ##
# MATLAB

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

def findNode(findData):
    global memory, head, current, pre
    current = head

    # 코드 작성 구간
    if current.data == findData:
        result = current
    else:
        find_flag = False
        while current.link != None:
            current = current.link
            if current.data == findData:
                result = current
                find_flag = True
                break

        if not find_flag:
            result = Node()
            
    return result


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

print('\n## R 검색 결과 ##')
f_node = findNode("R")
print(f_node.data)

print('## C++ 검색 결과 ##')
f_node = findNode("C++")
print(f_node.data)

print('## MATLAB 검색 결과 ##')
f_node = findNode("MATLAB")
print(f_node.data)

print('## Scala 검색 결과 ##')
f_node = findNode("Scala")
print(f_node.data)