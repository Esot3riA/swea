from collections import deque
import sys
sys.stdin = open("input.txt", 'r')

inf = 10000000

testCase = int(input())
for case in range(1, testCase + 1):
    N = int(input())
    region = [list(map(int, input().split())) for _ in range(N)]
    dist = [[inf] * N for _ in range(N)]
    dist[0][0] = 0

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    queue = deque()
    queue.append((0, 0))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            if 0 <= y + dy[i] < N and 0 <= x + dx[i] < N:
                height_diff = region[y + dy[i]][x + dx[i]] - region[y][x]
                if height_diff > 0:
                    cost = height_diff + 1
                else:
                    cost = 1

                if dist[y + dy[i]][x + dx[i]] > dist[y][x] + cost:
                    dist[y + dy[i]][x + dx[i]] = dist[y][x] + cost
                    queue.append((y + dy[i], x + dx[i]))

    print(dist)
    print("#{} {}".format(case, dist[N - 1][N - 1]))
