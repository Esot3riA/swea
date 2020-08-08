import sys
sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(1, testCase + 1):
    num = float(input())

    result = ""
    is_valid = False
    for i in range(12):
        num *= 2
        if num == 1:
            result += "1"
            is_valid = True
            break
        elif num > 1:
            result += "1"
            num -= 1
        else:
            result += "0"

    if is_valid:
        print("#{} {}".format(case, result))
    else:
        print("#{} overflow".format(case))
