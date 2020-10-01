import sys
sys.stdin = open("input.txt", 'r')


def hash_word(word):
    result = 0
    for j in range(len(word)):
        result += ord(word[j])
    return result


testCase = int(input())
for case in range(1, testCase + 1):
    N, M = map(int, input().split())
    wordA = [input() for _ in range(N)]
    wordB = [input() for _ in range(M)]

    hashA = [hash_word(wordA[i]) for i in range(N)]
    hashB = [hash_word(wordB[i]) for i in range(M)]

    commons = 0
    for i in range(N):
        for j in range(M):
            if hashA[i] == hashB[j]:
                if wordA[i] == wordB[j]:
                    commons += 1

    print("#{} {}".format(case, commons))
