import sys
sys.stdin = open("input.txt", 'r')


def calc_oil(position, charge_count, oil):
    global result
    if charge_count < result and oil >= 0:
        if position == N:
            result = charge_count
        elif position < N:
            calc_oil(position + 1, charge_count + 1, stations[position - 1] - 1)
            calc_oil(position + 1, charge_count, oil - 1)


testCase = int(input())
for case in range(1, testCase + 1):
    stations = list(map(int, input().split()))
    N = stations.pop(0)

    result = 1000
    calc_oil(2, 0, stations[0] - 1)

    print("#{} {}".format(case, result))
