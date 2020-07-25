import sys
sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(1, testCase + 1):
    N, M = map(int, input().split())
    sequence = list(map(int, input().split()))

    print("#{} {}".format(case, sequence[M % N]))
