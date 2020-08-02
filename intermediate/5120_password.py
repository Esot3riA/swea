import sys
sys.stdin = open("input.txt", 'r')


class Node:
    def __init__(self, val=None, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.next = nxt


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.curNode = None
        self.length = 0

    def add_node(self, val):
        node = Node(val, self.tail, self.head)
        if self.head is None:
            self.head = node
            self.tail = node
            self.curNode = node
        else:
            self.head.prev = node
            self.tail.next = node
            self.tail = node
        self.length += 1

    def insert_between_node(self, m):
        prev_node = self.curNode
        for i in range(m - 1):
            prev_node = prev_node.next
        next_node = prev_node.next

        new_node = Node(prev_node.val + next_node.val, prev_node, next_node)
        prev_node.next = new_node
        next_node.prev = new_node
        self.curNode = new_node
        self.length += 1
        if prev_node is self.tail:
            self.tail = new_node

    def print_all(self):
        node = self.head
        for i in range(self.length):
            print(node.val, end=' ')
            node = node.next
        print()

    def print_back_ten(self):
        node = self.tail
        for i in range(min(self.length, 10)):
            print(node.val, end=' ')
            node = node.prev
        print()


testCase = int(input())
for case in range(1, testCase + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))

    password = LinkedList()
    for element in arr:
        password.add_node(element)

    for j in range(K):
        password.insert_between_node(M)
    print("#{} ".format(case), end='')
    password.print_back_ten()
