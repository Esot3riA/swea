import sys
sys.stdin = open("input.txt", 'r')
inf = 1000

testCase = int(input())
for case in range(1, testCase + 1):
    V, E = map(int, input().split())
    V += 1
    w = [[inf] * V for _ in range(V)]
    for i in range(E):
        vertex1, vertex2, weight = map(int, input().split())
        w[vertex1][vertex2] = weight
        w[vertex2][vertex1] = weight

    result = 0
    distance = w[0]
    visited = [False] * V
    for i in range(V - 1):
        nearest = 0
        nearest_dist = inf
        for j in range(1, V):
            if not visited[j] and distance[j] < nearest_dist:
                nearest = j
                nearest_dist = distance[j]
        visited[nearest] = True
        result += nearest_dist
        for j in range(1, V):
            if w[nearest][j] < distance[j]:
                distance[j] = w[nearest][j]

    print("#{} {}".format(case, result))
