import sys
sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(1, testCase + 1):
    N, M, L = map(int, input().split())
    tree = [-1] * (N + 1)
    for i in range(M):
        leaf, val = map(int, input().split())
        tree[leaf] = val

    target = N
    while target > 0:
        if tree[target] == -1:
            if target * 2 == N:
                tree[target] = tree[target * 2]
            else:
                tree[target] = tree[target * 2] + tree[target * 2 + 1]
        if target is L:
            result = tree[target]
            break
        target -= 1
    print("#{} {}".format(case, result))
