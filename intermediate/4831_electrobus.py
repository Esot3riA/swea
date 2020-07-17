# import sys
# sys.stdin = open("input.txt", "r")

testCase = int(input())
for case in range(testCase):
    k, n, m = map(int, input().split())
    station = list(map(int, input().split()))
    station.insert(0, 0)
    station.append(n)

    isPossible = True
    result = 0
    currentOil = k
    for i in range(0, m + 1):
        nextMove = station[i + 1] - station[i]
        if nextMove > k:
            isPossible = False
            break
        if nextMove > currentOil:
            currentOil = k
            result += 1
        currentOil -= nextMove

    if isPossible:
        print("#{case} {result}".format(case=case + 1, result=result))
    else:
        print("#{case} {result}".format(case=case + 1, result=0))
