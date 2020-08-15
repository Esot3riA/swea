import sys
sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(1, testCase + 1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    volume = 0
    containers.sort(reverse=True)
    trucks.sort(reverse=True)
    for i in range(N):
        max_container = containers.pop(0)
        if trucks:
            if max_container <= trucks[0]:
                trucks.pop(0)
                volume += max_container

    print("#{} {}".format(case, volume))
