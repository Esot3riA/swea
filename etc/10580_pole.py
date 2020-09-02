import sys
sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(1, testCase + 1):
    N = int(input())
    lines = [tuple(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(i + 1, N):
            if lines[i][0] < lines[j][0] and lines[i][1] > lines[j][1]:
                result += 1
            elif lines[i][0] > lines[j][0] and lines[i][1] < lines[j][1]:
                result += 1

    print("#{} {}".format(case, result))
