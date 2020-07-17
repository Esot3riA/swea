import sys
sys.stdin = open("input.txt", 'r')


def getPaperCnt(width):
    if width == n:
        return 1
    elif width > n:
        return 0
    return getPaperCnt(width + 10) + (getPaperCnt(width + 20) * 2)


testCase = int(input())
for case in range(testCase):
    n = int(input())
    result = getPaperCnt(0)
    print("#{} {}".format(case+1, result))
