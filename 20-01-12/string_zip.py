#https://programmers.co.kr/learn/courses/30/lessons/60057

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
                count = 1
                pre_s = now_s
            if len(pre_s) > len(s):
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
#느낀 점
# interval 변수에 주의
# 문제 설명 동영상 (16분) 짜리를 4번을  보아서 이해 했다.