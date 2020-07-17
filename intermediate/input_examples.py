arr = [0] * 5
arr2 = [i for i in range(2, 9) if i % 2 == 0]

brr = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
brr2 = [[1, 2, 3]] * 3
brr3 = [[1, 2, 3] for _ in range(3)]
brr4 = [[i, j] for i in range(3) for j in range(3)]

n, m = map(int, input().split())
mylist = [list(map(int, input().split())) for _ in range(n)]

newlist = [(i, j) for i in range(n) for j in range(m) if mylist[i][j] == 1]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for x in range(len(brr)):
    for y in range(len(brr[x])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            print(brr[testX][testY])

alpha = ['a', 'b', 'c']
index = [1, 2, 3]
alpha_index = list(zip(alpha, index))
