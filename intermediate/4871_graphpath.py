import sys
sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(testCase):
    v, e = map(int, input().split())
    edges = {}
    for i in range(v):
        edges[i + 1] = [i + 1]
    for i in range(e):
        node1, node2 = map(int, input().split())
        newEdges = edges[node1]
        newEdges.append(node2)
        edges[node1] = newEdges
    s, g = map(int, input().split())

    result = 0
    toVisit = [s]
    visited = []
    while toVisit:
        currentNode = toVisit.pop()
        visited.append(currentNode)
        belowNodes = edges[currentNode]
        for belowNode in belowNodes:
            if belowNode not in visited:
                toVisit.append(belowNode)
        if currentNode == g:
            result = 1

    print("#{} {}".format(case + 1, result))
