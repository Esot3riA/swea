import sys
sys.stdin = open("input.txt", 'r')


class Node:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.next = nxt


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_node(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def insert_node(self, index, val):
        target_node = self.find_node(index)
        new_node = Node(val, target_node.next)
        target_node.next = new_node
        self.length += 1

    def delete_node(self, index):
        target_node = self.find_node(index)
        target_node.next = target_node.next.next
        self.length -= 1

    def replace_node(self, index, val):
        target_node = self.find_node(index)
        target_node.next.val = val

    def find_node(self, index):
        target_node = self.head
        for j in range(index - 1):
            target_node = target_node.next
        return target_node

    def print_node(self, index):
        if self.length <= index:
            print("-1")
        else:
            print(self.find_node(index).next.val)


testCase = int(input())
for case in range(1, testCase + 1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))

    sequence = LinkedList()
    for i in range(N):
        sequence.add_node(arr[i])

    for i in range(M):
        operation_str = input().split()
        if operation_str[0] is "I":
            sequence.insert_node(int(operation_str[1]), int(operation_str[2]))
        elif operation_str[0] is "D":
            sequence.delete_node(int(operation_str[1]))
        elif operation_str[0] is "C":
            sequence.replace_node(int(operation_str[1]), int(operation_str[2]))

    print("#{} ".format(case), end='')
    sequence.print_node(L)
