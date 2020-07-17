import sys
sys.stdin = open("input.txt", 'r')


def promising(y, x):
    return 0 <= y < N and 0 <= x < N and (Maze[y][x] == 0 or Maze[y][x] == 3)


def DFS(y, x):
    global result
    if Maze[y][x] == 3:
        result = 1
        return

    visited[y][x] = 1
    for dir in range(4):
        new_y = y + dy[dir]
        new_x = x + dx[dir]
        if promising(new_y, new_x) and not visited[new_y][new_x]:
            DFS(new_y, new_x)


testCase = int(input())
for case in range(1, testCase + 1):
    N = int(input())
    Maze = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if Maze[i][j] == 2:
                start_y, start_x = i, j

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    visited = [[0] * N for _ in range(N)]
    result = 0
    DFS(start_y, start_x)
    print("#{} {}".format(case, result))
