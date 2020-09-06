import sys
sys.stdin = open("input.txt", 'r')

inf = 1000

testCase = int(input())
for case in range(1, testCase + 1):
    N, E = map(int, input().split())
    N += 1
    weight = [[inf] * N for _ in range(N)]
    for i in range(E):
        start, end, w = map(int, input().split())
        weight[start][end] = w

    distance = weight[0]
    touch = [0] * N
    for i in range(N - 1):
        nearest = -1
        nearest_dist = inf
        for j in range(1, N):
            if distance[j] < nearest_dist and distance[j] != -1:
                nearest = j
                nearest_dist = distance[j]

        if nearest == N - 1:
            break
        else:
            distance[nearest] = -1

        for j in range(1, N):
            if distance[j] > nearest_dist + weight[nearest][j]:
                distance[j] = nearest_dist + weight[nearest][j]
                touch[j] = nearest

    print("#{} {}".format(case, distance[N - 1]))
