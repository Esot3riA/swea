import sys
sys.stdin = open("input.txt", 'r')


def binary_search(key):
    global result
    l = 0
    r = N - 1
    direction_flag = 0
    while l <= r:
        m = (l + r) // 2
        if listA[m] == key:
            if direction_flag != -1:
                result += 1
            return
        elif listA[m] < key:
            l = m + 1
            if direction_flag == 0 or direction_flag == 2:
                direction_flag = 1
            else:
                direction_flag = -1
        else:
            r = m - 1
            if direction_flag == 0 or direction_flag == 1:
                direction_flag = 2
            else:
                direction_flag = -1


testCase = int(input())
for case in range(1, testCase + 1):
    N, M = map(int, input().split())
    listA = list(map(int, input().split()))
    listB = list(map(int, input().split()))

    listA.sort()
    result = 0
    for target in listB:
        binary_search(target)

    print("#{} {}".format(case, result))
