# import sys
# sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(testCase):
    board = [[0] * 10 for _ in range(10)]
    n = int(input())
    for i in range(n):
        startX, startY, endX, endY, color = map(int, input().split())
        for y in range(startY, endY + 1):
            for x in range(startX, endX + 1):
                board[y][x] += color

    result = 0
    for y in range(10):
        for x in range(10):
            if board[y][x] == 3:
                result += 1

    print("#{case} {result}".format(case=case + 1, result=result))
