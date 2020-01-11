# 4번째
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])



# 3번째 
# https://www.youtube.com/watch?v=dLnMYhb-jBQ&feature=emb_logo
# 이 영상을 3번 보았다. ㅠㅠ 
def solution(s):
    if len(s) < 3:
        return len(s)
    answer = len(s) # 기본 Value
    max_cand = int(len(s) / 2)
    for interval in range(1, max_cand+1):
        pre_s = s[0:interval]
        start = interval
        res = []
        count = 1
        while True:
            now_s = s[start:start+interval]
            if now_s == pre_s:
                count += 1
            else:
                res.append([count, pre_s])
                num = 1
                pre_s = now_s
            if start > len(s):
                break
            start += interval
        len_cand = 0
        for k in range(len(res)):
            if res[k][0] == 1:
                len_cand += len(res[k][1])
            else:
                len_cand += len(str(res[k][0]))
                len_cand += len(res[k][1])
        answer = min(answer, len_cand)
     return answer   





# 두 번째 시도 :  0점 
def solution(s):
    answer = 0
    for i in range(1,len(s) + 1):
        note = i
        compare_list = list()
        chunks = [s[i:i+note] for i in range(0, len(s), note)]
        print(chunks)
        for idx, chunk_item in enumerate(chunks):
            count = 0
            if(idx + 1 < (len(chunks) - 1)):
                if(chunk_item == chunks[idx + 1]):
                    count =  count + 1
                    if(count > 1):
                        answer += len(str(count) + str(chunk_item))
                    else:
                        answer += len(str(chunk_item))
                        
                else:
                    answer += len(chunks[idx + 1])
            if (idx + 1 == (len(chunks) - 1)):
                pass
                
            compare_list.append(answer)

    answer = min(ele for ele in compare_list)

            
    return answer

# 첫번째 시도 :런타임 에러 
def solution(s):
    answer = 0
    for i in range(1,len(s) + 1):
        note = i
        compare_list = list()
        chunks = [s[i:i+note] for i in range(0, len(s), note)]
        
        for idx, chunk_item in enumerate(chunks):

            count = 0
            while(idx + 1 < (len(chunks) - 1)):
                if(chunk_item == chunks[idx + 1]):
                    count =  count + 1
                    answer += len(str(count) + str(chunk_item))
                else:
                    answer += len(chunks[idx + 1])
            if (idx + 1 == (len(chunks) - 1)):
                pass
                
            compare_list.append(answer)
    answer = sorted(compare_list, key=len)[0]
            
    return answer