# import sys
# sys.stdin = open("input.txt", "r")

totalCase = int(input())
for case in range(totalCase):
    input_count = int(input())
    inputs = list(map(int, input().split()))

    min = inputs[0]
    max = inputs[0]
    for i in range(1, input_count):
        if min > inputs[i]:
            min = inputs[i]
        if max < inputs[i]:
            max = inputs[i]
    result = max - min
    print("#{case} {result}".format(case=case+1, result=result))
