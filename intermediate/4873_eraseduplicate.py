import sys
sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(testCase):
    text = input()

    chars = [text[0]]
    for i in range(1, len(text)):
        if len(chars) > 0:
            targetChar = chars.pop()
            if targetChar != text[i]:
                chars.append(targetChar)
                chars.append(text[i])
        else:
            chars.append(text[i])

    print("#{} {}".format(case + 1, len(chars)))
