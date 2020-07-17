import sys
sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(testCase):
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]

    result = ""
    for row in range(n):
        for col in range(n - m + 1):
            isAnswer = True
            for i in range(int(m / 2)):
                if board[row][col + i] != board[row][col + m - i - 1]:
                    isAnswer = False
            if isAnswer:
                result = board[row][col:col + m]
    for row in range(n - m + 1):
        for col in range(n):
            isAnswer = True
            for i in range(int(m / 2)):
                if board[row + i][col] != board[row + m - i - 1][col]:
                    isAnswer = False
            if isAnswer:
                for i in range(m):
                    result += board[row + i][col]
    print("#{case} {result}".format(case=case + 1, result=result))
