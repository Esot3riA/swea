import sys
sys.stdin = open("input.txt", 'r')


def promising(y, x):
    return (0 <= y < N and 0 <= x < N) and (maze[y][x] == 0 or maze[y][x] == 3) and not visited[y][x]


def DFS(y, x, depth):
    global distance, visited
    if promising(y, x):
        visited[y][x] = 1
        if maze[y][x] == 3 and distance > depth:
            distance = depth
        for k in range(4):
            DFS(y + dy[k], x + dx[k], depth + 1)


testCase = int(input())
for case in range(1, testCase + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_y = i
                start_x = j
                maze[i][j] = 0

    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    distance = 10000
    DFS(start_y, start_x, -1)

    if distance == 10000:
        distance = 0
    print("#{} {}".format(case, distance))
