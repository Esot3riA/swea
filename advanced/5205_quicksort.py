import sys
sys.stdin = open("input.txt", 'r')


def quicksort(start, end):
    if start >= end:
        return

    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    quicksort(start, i)
    quicksort(i + 2, end)


testCase = int(input())
for case in range(1, testCase + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    quicksort(0, N - 1)
    print("#{} {}".format(case, arr[N // 2]))
