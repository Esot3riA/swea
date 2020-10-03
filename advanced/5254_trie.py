import sys
sys.stdin = open("input.txt", 'r')


def long_comp_pref(word1,word2):
    word1_len=len(word1)
    word2_len=len(word2)
    min_len=min(word1_len,word2_len)


    for cnt in range(min_len):
        if word1[:cnt+1]!= word2[:cnt+1]:
            break
    return cnt


def find_n_th_partial_word(words,n,max_len):
    i=0
    words_len=len(words)
    lcp=0

    while(i<words_len):
        cur_idx,cur_suf=words[i]
        candidates_num=max_len-cur_idx
        # 이전 suffix의 부분문자열과 중복되지 않는 현재 suffix의 부분 문자열의 실제 갯수 = candidates_num - lcp
        if candidates_num-lcp >= n:
            # suffix의 prefix는 길이가 짧을 수록 사전순으로 정렬시 먼저 온다.
            # 중복된 경우를 제외할 경우 n번째 부분 문자열은 n+lcp 번째 prefix이다.
            return cur_suf, len(cur_suf[:n+lcp])
        else:
            n-= (candidates_num-lcp)
            if i!=(words_len-1):
                lcp=long_comp_pref(cur_suf,words[i+1][1]) #cur_suf=words[i][1]
            i+=1
    return 0,0


for t in range(1, int(input())+1):
    str_N,word=input().split()
    word_len=len(word)

    # ordered_suffixes의 요소들은 서로 구분가능 하다 (길이가 모두 다르기 때문).
    unordered_suffixes=[(i,word[i:]) for i in range(word_len)]
    ordered_suffixes=sorted(unordered_suffixes,key = lambda elements: elements[1])
    partial_word, its_len=find_n_th_partial_word(ordered_suffixes,int(str_N),word_len)
    print('#{} {} {}'.format(t,partial_word[0],its_len))