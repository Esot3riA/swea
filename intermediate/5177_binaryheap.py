import sys
sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(1, testCase + 1):
    N = int(input())
    input_values = list(map(int, input().split()))

    count = 0
    min_heap = [-1] * (N + 1)
    for i in range(N):
        count += 1
        min_heap[count] = input_values[i]

        pointer = count
        while pointer > 1:
            parent_pointer = pointer // 2
            if min_heap[parent_pointer] > min_heap[pointer]:
                tmp = min_heap[pointer]
                min_heap[pointer] = min_heap[parent_pointer]
                min_heap[parent_pointer] = tmp
            pointer = pointer // 2

    result = 0
    ancestor = N // 2
    while ancestor > 0:
        result += min_heap[ancestor]
        ancestor = ancestor // 2
    print("#{} {}".format(case, result))
