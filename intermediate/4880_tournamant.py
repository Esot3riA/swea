import sys
sys.stdin = open("input.txt", 'r')


def dfs(start, end):
    if end - start == 0:
        return start
    elif end - start == 1:
        return battle(start, end)
    else:
        center = (start + end) // 2
        return battle(dfs(start, center), dfs(center + 1, end))


def battle(std1, std2):
    if (cards[std1] == 1 and cards[std2] == 2) \
            or (cards[std1] == 2 and cards[std2] == 3) \
            or (cards[std1] == 3 and cards[std2] == 1):
        winner = std2
    else:
        winner = std1
    return winner


testCase = int(input())
for case in range(1, testCase + 1):
    N = int(input())
    cards = list(map(int, input().split()))

    print("#{} {}".format(case, dfs(0, N - 1) + 1))
