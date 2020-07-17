import sys
sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(testCase):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    min = sys.maxsize
    max = 0
    for i in range(n - m + 1):
        sum = 0
        for j in range(i, i + m):
            sum += arr[j]
        if min > sum:
            min = sum
        if max < sum:
            max = sum

    result = max - min
    print("#{case} {result}".format(case=case + 1, result=result))
