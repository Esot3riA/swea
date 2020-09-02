import sys
sys.stdin = open("input.txt", 'r')


def promising(level, cols, total_cost):
    if total_cost > min_cost:
        return False

    is_promising = True
    for j in range(level):
        if cols[j] == cols[level]:
            is_promising = False
    return is_promising


def calc_cost(level, cols, total_cost):
    global min_cost
    if promising(level, cols, total_cost):
        if level == N - 1:
            min_cost = total_cost
        elif level < N - 1:
            for j in range(N):
                cols[level + 1] = j + 1
                calc_cost(level + 1, cols, total_cost + costs[level + 1][j])


testCase = int(input())
for case in range(1, testCase + 1):
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]

    min_cost = 100000
    cols = [0] * N
    calc_cost(-1, cols, 0)

    print("#{} {}".format(case, min_cost))
