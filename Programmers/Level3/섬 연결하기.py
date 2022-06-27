# 크루스칼 알고리즘 (Kruskal Algorithm)

def find(n):
    if (n == node_list[n]):
        return n
    else:
        return find(node_list[n])


def unionParent(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        node_list[b] = a
    else:
        node_list[a] = b


def compareParent(a, b):
    # 최상위 노드 검색, 같을 경우 사이클이므로 수행 X
    a = find(a)
    b = find(b)
    if a == b:
        return True
    else:
        return False


def solution(n, costs):
    global node_list
    answer = 0
    node_list = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])

    for parent, child, cost in costs:
        if not compareParent(parent, child):
            answer += cost
            unionParent(parent, child)

    return answer
