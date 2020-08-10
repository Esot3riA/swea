import sys
sys.stdin = open("input.txt", 'r')


def DFS(y, x, cost):
    global min_val
    if y < N and x < N and cost < min_val:
        cost += board[y][x]
        if (y == N - 1 and x == N - 1) and min_val > cost:
            min_val = cost
        else:
            for i in range(2):
                DFS(y + dy[i], x + dx[i], cost)


testCase = int(input())
for case in range(1, testCase + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    dy = [1, 0]
    dx = [0, 1]
    min_val = 10000
    DFS(0, 0, 0)

    print("#{} {}".format(case, min_val))
