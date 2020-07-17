import sys
sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(testCase):
    codes = input().split()
    operators = ['+', '-', '*', '/']
    numStack = []

    result = ""
    for code in codes:
        if code == '.':
            if len(numStack) == 1:
                result = int(numStack.pop())
                break
            else:
                result = "error"
                break
        elif code.isdigit():
            numStack.append(int(code))
        elif code in operators:
            if len(numStack) < 2:
                result = "error"
                break
            targetNum = numStack.pop()
            sourceNum = numStack.pop()
            if code == '+':
                numStack.append(sourceNum + targetNum)
            elif code == '-':
                numStack.append(sourceNum - targetNum)
            elif code == '*':
                numStack.append(sourceNum * targetNum)
            elif code == '/':
                numStack.append(sourceNum / targetNum)

    print("#{} {}".format(case + 1, result))
