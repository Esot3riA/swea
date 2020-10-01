from collections import deque
import sys
sys.stdin = open("input.txt", 'r')


class Node:
    def __init__(self, data):
        self.data = data
        self.full_str = None
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, str):
        curr_node = self.head
        for char in str:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        curr_node.full_str = str

    def find_substr(self, n):
        # DFS
        substr_count = 0
        queue = deque()
        queue.append(self.head)
        while queue:
            cur_node = queue.pop()
            if cur_node.data == "$":
                substr_count += 1
                if substr_count == n:
                    return cur_node.full_str

            node_keys = list(cur_node.children.keys())
            node_keys.sort(reverse=True)
            for key in node_keys:
                queue.append(cur_node.children[key])


testCase = int(input())
for case in range(1, testCase + 1):
    N, input_str = input().split()
    str_len = len(input_str)

    trie = Trie()
    for i in range(str_len):
        for j in range(i + 1, str_len + 1):
            substr = input_str[i:j] + "$"
            trie.insert(substr)

    result_str = trie.find_substr(int(N))
    print("#{} {} {}".format(case, result_str[0], len(result_str) - 1))
