import sys
sys.stdin = open("input.txt", 'r')


def merge(left, right):
    global merge_count
    i, j = 0, 0
    left_size = len(left)
    right_size = len(right)
    merged_arr = []

    if left[left_size - 1] > right[right_size - 1]:
        merge_count += 1

    while i < left_size and j < right_size:
        if left[i] < right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1

    if i == left_size:
        merged_arr.extend(right[j:right_size])
    if j == right_size:
        merged_arr.extend(left[i:left_size])
    return merged_arr


def mergesort(start, end):
    if start == end:
        return [arr[start]]

    mid = start + ((end - start - 1) // 2)
    left = mergesort(start, mid)
    right = mergesort(mid + 1, end)
    return merge(left, right)


testCase = int(input())
for case in range(1, testCase + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    merge_count = 0
    result = mergesort(0, N - 1)
    print("#{} {} {}".format(case, result[N // 2], merge_count))
