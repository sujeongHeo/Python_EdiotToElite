#https://programmers.co.kr/learn/courses/30/lessons/42840/solution_groups?language=python3
def solution(answers):
    p = [[1,2,3,4,5],
         [2,1,2,3,2,4,2,5]
         [3,3,1,1,2,2,4,4,5,5]]
    s = [0] * len(p)

    for q,a in enumerate(answers):
        for i,v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1,for i, v in enumerate(s) if v == max(s)]

    # 내 풀이

    def solution(answers):
    scores = [0,0,0]
    answer = []
    pattern1 = range(1,6)
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i] == pattern1[i % len(pattern1)]:
            scores[0] += 1
        if answers[i] == pattern2[i % len(pattern2)]:
            scores[1] += 1
        if answers[i] == pattern3[i % len(pattern3)]:
            scores[2] += 1
    for i,v in enumerate(scores):
        if (max(scores) == scores[i]):
            answer.append(i+1)
    return answer