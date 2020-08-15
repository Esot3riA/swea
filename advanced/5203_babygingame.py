import sys
sys.stdin = open("input.txt", 'r')


def check_babygin(id, hands):
    global result
    hand_size = len(hands)
    if hand_size >= 3:
        for num in range(0, 10):
            if hands.count(num) >= 3:
                result = id
                return
        for num in range(0, 8):
            if hands.count(num) and hands.count(num + 1) and hands.count(num + 2):
                result = id
                return


testCase = int(input())
for case in range(1, testCase + 1):
    cards = list(map(int, input().split()))
    player1 = []
    player2 = []

    result = 0
    while cards:
        player1.append(cards.pop(0))
        check_babygin(1, player1)
        if result:
            break
        player2.append(cards.pop(0))
        check_babygin(2, player2)
        if result:
            break

    print("#{} {}".format(case, result))
