import sys
sys.stdin = open("input.txt", 'r')


class Node:
    def __init__(self):
        self.nodes = []


testCase = int(input())
for case in range(1, testCase + 1):
    E, N = map(int, input().split())
    edges_input = list(map(int, input().split()))
    tree = [Node() for _ in range(E + 2)]
    for i in range(E):
        tree[edges_input[i * 2]].nodes.append(edges_input[(i * 2) + 1])

    target_nodes = [N]
    count = 0
    while target_nodes:
        cur_node = tree[target_nodes.pop(0)]
        for i in range(len(cur_node.nodes)):
            target_nodes.append(cur_node.nodes[i])
        count += 1

    print("#{} {}".format(case, count))
