# import sys
# sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(testCase):
    n, k = map(int, input().split())

    result = 0
    for i in range(1 << 12):
        elements = 0
        sum = 0
        for j in range(12):
            if (i >> j) % 2 == 1:
               elements += 1
               sum += (j + 1)
        if elements == n and sum == k:
            result += 1

    print("#{case} {result}".format(case=case + 1, result=result))
