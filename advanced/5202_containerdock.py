import sys
sys.stdin = open("input.txt", 'r')
import heapq


testCase = int(input())
for case in range(1, testCase + 1):
    N = int(input())
    schedules = [tuple(map(int, input().split())) for _ in range(N)]

    estimated_times = [schedule[1] - schedule[0] for schedule in schedules]
    time_heap = []
    for i in range(N):
        heapq.heappush(time_heap, (estimated_times[i], i))

    time = [0] * 24
    tasks = 0
    while time_heap:
        task_idx = heapq.heappop(time_heap)[1]
        start_time = schedules[task_idx][0]
        end_time = schedules[task_idx][1]

        is_time_empty = True
        for i in range(estimated_times[task_idx]):
            if time[start_time + i] == 1:
                is_time_empty = False
                break
        if is_time_empty:
            for i in range(start_time, end_time):
                time[i] = 1
            tasks += 1

    print("#{} {}".format(case, tasks))
