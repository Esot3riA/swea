import sys
sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(testCase):
    code = input()
    brackets = []
    openBrackets = ['(', '{', '[']
    closeBrackets = [')', '}', '[']

    result = 1
    for i in range(len(code)):
        if code[i] in openBrackets:
            brackets.append(code[i])
        elif code[i] in closeBrackets:
            if len(brackets) <= 0:
                result = 0
                break
            bracket = brackets.pop()
            if (bracket == '(' and code[i] != ')') \
                    or (bracket == '{' and code[i] != '}') \
                    or (bracket == '[' and code[i] != ']'):
                result = 0
                break
    if len(brackets) > 0:
        result = 0

    print("#{} {}".format(case + 1, result))
