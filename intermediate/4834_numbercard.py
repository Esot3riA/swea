# import sys
# sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(testCase):
    cardNum = int(input())
    cards = input()

    counter = [0 for tmp in range(10)]
    for i in range(cardNum):
        targetCard = int(cards[i])
        counter[targetCard] += 1

    maxNum = 0
    maxNumCnt = counter[0]
    for i in range(1, 10):
        if counter[i] >= maxNumCnt:
            maxNum = i
            maxNumCnt = counter[i]

    print("#{case} {maxNum} {maxNumCnt}"
          .format(case=case + 1, maxNum=maxNum, maxNumCnt=maxNumCnt))
