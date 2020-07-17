import sys
sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(testCase):
    str1 = input()
    str2 = input()
    charCnts = {}

    for i in range(len(str1)):
        charCnts[str1[i]] = 0
    for i in range(len(str2)):
        if str2[i] in charCnts:
            charCnts[str2[i]] += 1
    result = max(charCnts.values())

    print("#{case} {result}".format(case=case+1, result=result))
