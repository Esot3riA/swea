import sys
sys.stdin = open("input.txt", 'r')


def inorder(index):
    global tree, num
    # Left
    if (index * 2) <= N:
        inorder(index * 2)
    # Center
    tree[index] = num
    num += 1
    # Right
    if (index * 2) + 1 <= N:
        inorder((index * 2) + 1)


testCase = int(input())
for case in range(1, testCase + 1):
    N = int(input())
    tree = [0] * (N + 1)
    num = 1

    inorder(1)
    print("#{} {} {}".format(case, tree[1], tree[N // 2]))
