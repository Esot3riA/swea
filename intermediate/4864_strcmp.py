import sys
sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(testCase):
    str1 = input()
    str2 = input()
    str1Len = len(str1)
    str2Len = len(str2)

    pointer = 0
    result = 0
    while pointer + str1Len <= str2Len and not result:
        move = False
        for i in range(str1Len):
            if str1[i] != str2[pointer + i]:
                move = True
                break
        if not move:
            result = 1
        else:
            pointer += 1

    print("#{case} {result}".format(case=case + 1, result=result))
