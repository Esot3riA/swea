import itertools
import sys
sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(1, testCase + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    min_battery = 10000
    areas = [i for i in range(1, N)]
    roots = list(itertools.permutations(areas))
    for root in roots:
        position = 0
        battery = 0
        for room in root:
            battery += board[position][room]
            position = room
        battery += board[position][0]
        if min_battery > battery:
            min_battery = battery

    print("#{} {}".format(case, min_battery))
