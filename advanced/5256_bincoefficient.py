import sys
sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(1, testCase + 1):
    n, a, b = map(int, input().split())

    memo = [[1] * i for i in range(1, n + 2)]
    for i in range(2, n + 1):
        for j in range(i):
            if (i - 1 >= 0) and (j - 1 >= 0):
                memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]

    print("#{} {}".format(case, memo[n][a]))
