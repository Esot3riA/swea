import sys
sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(1, testCase + 1):
    digit, hex_str = input().split()

    result = ""
    for i in range(int(digit)):
        hex_val = int(hex_str[i], 16)
        hex_result = ""
        for j in range(4):
            hex_result = str(hex_val % 2) + hex_result
            hex_val = hex_val // 2
        result += hex_result

    print("#{} {}".format(case, result))
