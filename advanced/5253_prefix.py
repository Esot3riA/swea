import sys
sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(1, testCase + 1):
    N, M = map(int, input().split())
    prefixes = set()
    for i in range(N):
        word = input()
        for j in range(1, len(word) + 1):
            prefixes.add(word[0:j])

    result = 0
    for i in range(M):
        prefix = input()
        if prefix in prefixes:
            result += 1

    print("#{} {}".format(case, result))
