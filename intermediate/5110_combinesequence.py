import sys
sys.stdin = open("input.txt", 'r')


class Node:
    def __init__(self, data=None, prev=None, nxt=None):
        self.data = data
        self.prev = prev
        self.next = nxt


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def init_nodes(self, seq):
        for i in range(len(seq)):
            if self.head is None:
                self.head = Node(seq[i], None, None)
                self.tail = self.head
            else:
                node = Node(seq[i], self.tail, None)
                self.tail.next = node
                self.tail = node

    def combine_list(self, other_list):
        target_num = other_list.head.data
        self_node = self.head
        combined = False
        while not combined and self_node is not None:
            if self_node.data > target_num:
                if self_node is self.head:
                    other_list.tail.next = self.head
                    self.head.prev = other_list.tail
                    self.head = other_list.head
                else:
                    other_list.head.prev = self_node.prev
                    other_list.tail.next = self_node
                    self_node.prev.next = other_list.head
                    self_node.prev = other_list.tail
                combined = True
            else:
                self_node = self_node.next
        if not combined:
            other_list.head.prev = self.tail
            self.tail.next = other_list.head
            self.tail = other_list.tail

    def print_nodes(self):
        node = self.tail
        for i in range(10):
            print(node.data, end=' ')
            node = node.prev
        print()


testCase = int(input())
for case in range(1, testCase + 1):
    N, M = map(int, input().split())
    sequence = list(map(int, input().split()))
    linked_list = LinkedList()
    linked_list.init_nodes(sequence)

    for j in range(M - 1):
        new_sequence = list(map(int, input().split()))
        new_linked_list = LinkedList()
        new_linked_list.init_nodes(new_sequence)
        linked_list.combine_list(new_linked_list)

    print("#{}".format(case), end=' ')
    linked_list.print_nodes()
