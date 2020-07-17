import sys
sys.stdin = open("input.txt", 'r')


def promising(cols, val, row):
    is_promising = True
    cols_set = set()
    for i in range(row):
        if cols[i] in cols_set:
            is_promising = False
        else:
            cols_set.add(cols[i])

    return val < min_val and is_promising


def dfs(cols, val, row):
    global min_val
    if promising(cols, val, row):
        if row == N and min_val > val:
            min_val = val
        elif row < N:
            for i in range(N):
                cols[row] = i
                dfs(cols, val + arr[row][i], row + 1)


testCase = int(input())
for case in range(1, testCase + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    selects = [-1] * N
    min_val = 1000
    dfs(selects, 0, 0)
    print("#{} {}".format(case, min_val))
