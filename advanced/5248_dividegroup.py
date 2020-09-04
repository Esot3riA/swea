import sys
sys.stdin = open("input.txt", 'r')


class Node:
    def __init__(self, val):
        self.parent = self
        self.val = val
        self.rank = 0

    def find_top(self):
        if self.parent != self:
            self.parent = self.parent.find_top()
        return self.parent

    def connect(self, node):
        self_top = self.find_top()
        node_top = node.find_top()
        if self_top.rank < node_top.rank:
            self_top.parent = node_top
        elif self_top.rank == node_top.rank:
            node_top.parent = self_top
            self_top.rank += 1
        else:
            node_top.parent = self_top


testCase = int(input())
for case in range(1, testCase + 1):
    N, M = map(int, input().split())
    input_stream = list(map(int, input().split()))
    nodes = [Node(i) for i in range(N + 1)]

    for i in range(M):
        num1, num2 = input_stream[i * 2], input_stream[i * 2 + 1]
        nodes[num1].connect(nodes[num2])

    nodes.pop(0)
    top_list = []
    for i in range(N):
        top_val = nodes[i].find_top().val
        if not top_list.count(top_val):
            top_list.append(top_val)
    print("#{} {}".format(case, len(top_list)))
