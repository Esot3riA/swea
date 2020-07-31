import sys
sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(1, testCase + 1):
    N, M, L = map(int, input().split())
    sequence = list(map(int, input().split()))

    for i in range(M):
        idx, num = map(int, input().split())
        sequence.insert(idx, num)

    print("#{} {}".format(case, sequence[L]))
