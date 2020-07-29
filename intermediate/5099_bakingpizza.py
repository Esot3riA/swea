import sys
sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(1, testCase + 1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    firepot = []
    baked_pizza = []
    i = 1
    for i in range(1, N + 1):
        firepot.append((i, pizza.pop(0)))

    # Run cycle
    while firepot:
        target_pizza = firepot.pop(0)
        target_pizza = (target_pizza[0], int(target_pizza[1] / 2))

        if target_pizza[1] <= 0:
            baked_pizza.append(target_pizza[0])
            if pizza:
                i += 1
                firepot.append((i, pizza.pop(0)))
        else:
            firepot.append(target_pizza)

    print("#{} {}".format(case, baked_pizza.pop(len(baked_pizza) - 1)))
