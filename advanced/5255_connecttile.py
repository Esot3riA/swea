import sys
sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(1, testCase + 1):
    N = int(input())

    memo = [0] * 31
    memo[0] = 1
    memo[1] = 1
    memo[2] = 3
    for i in range(3, N + 1):
        memo[i] = memo[i - 1] + (2 * memo[i - 2]) + memo[i - 3]

    print("#{} {}".format(case, memo[N]))
