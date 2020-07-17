import sys
sys.stdin = open("input.txt", 'r')

testCase = int(input())
for case in range(testCase):
    totalPage, aPage, bPage = map(int, input().split())

    aLeft, aCurrentPage, aRight = (1, totalPage / 2, totalPage)
    bLeft, bCurrentPage, bRight = (1, totalPage / 2, totalPage)
    isAFind = False
    isBFind = False

    while not (isAFind or isBFind):
        if aCurrentPage > aPage:
            aRight = aCurrentPage
            aCurrentPage = int((aLeft + aCurrentPage) / 2)
        elif aCurrentPage < aPage:
            aLeft = aCurrentPage
            aCurrentPage = int((aCurrentPage + aRight) / 2)
        else:
            isAFind = True

        if bCurrentPage > bPage:
            bRight = bCurrentPage
            bCurrentPage = int((bLeft + bCurrentPage) / 2)
        elif bCurrentPage < bPage:
            bLeft = bCurrentPage
            bCurrentPage = int((bCurrentPage + bRight) / 2)
        else:
            isBFind = True

    result = -1
    if isAFind and isBFind:
        result = "0"
    elif isAFind:
        result = "A"
    elif isBFind:
        result = "B"
    print("#{case} {result}".format(case=case + 1, result=result))
