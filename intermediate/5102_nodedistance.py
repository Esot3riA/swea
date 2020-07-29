import sys
sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(1, testCase + 1):
    V, E = map(int, input().split())

    edges = [[0] * V for _ in range(V)]
    for i in range(V):
        edges[i][i] = 1
    for i in range(E):
        node1, node2 = map(int, input().split())
        edges[node1 - 1][node2 - 1] = 1
        edges[node2 - 1][node1 - 1] = 1
    start_node, end_node = map(int, input().split())

    result = 0
    visited = [0] * V
    visit_queue = [(start_node, 0)]
    while visit_queue:
        target_node = visit_queue.pop(0)
        visited[target_node[0] - 1] = 1
        if target_node[0] is end_node:
            result = target_node[1]
            break
        for j in range(V):
            if edges[target_node[0] - 1][j] \
                    and j is not target_node[0] - 1\
                    and not visited[j]:
                visit_queue.append((j + 1, target_node[1] + 1))

    print("#{} {}".format(case, result))
