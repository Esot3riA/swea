from collections import deque
import sys
sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(1, testCase + 1):
    N, M = map(int, input().split())

    limit = 1000001
    queue = deque()
    queue.append((N, 0))
    visited = [False] * limit
    while queue:
        num, level = queue.popleft()
        visited[num] = True
        if num == M:
            print("#{} {}".format(case, level))
            break

        target = num + 1
        if target < limit and not visited[target]:
            queue.append((target, level + 1))
            visited[target] = True
        target = num - 1
        if target > 0 and not visited[target]:
            queue.append((target, level + 1))
            visited[target] = True
        target = num * 2
        if target < limit and not visited[target]:
            queue.append((target, level + 1))
            visited[target] = True
        target = num - 10
        if target > 0 and not visited[target]:
            queue.append((target, level + 1))
            visited[target] = True
