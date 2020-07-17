import sys
sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(testCase):
    numbersCnt = int(input())
    numbers = list(map(int, input().split()))
    print("#{case}".format(case=case + 1), end='')
    for i in range(10):
        if (i % 2) == 0:
            maxValue = max(numbers)
            numbers.remove(maxValue)
            print(" {maxValue}".format(maxValue=maxValue), end='')
        else:
            minValue = min(numbers)
            numbers.remove(minValue)
            print(" {minValue}".format(minValue=minValue), end='')
    print("")
