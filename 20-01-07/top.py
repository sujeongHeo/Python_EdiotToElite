'''
https://programmers.co.kr/learn/courses/30/lessons/42588

입출력 예
heights	return
[6,9,5,7,4]	[0,0,2,2,4]
[3,9,9,3,5,7,2]	[0,0,0,3,3,3,6]
[1,5,3,6,7,6,5]	[0,0,2,0,0,5,6]
'''
# 4번째 작성 정확도 100
def solution(heights):
    answer = []
    note = ''
    for idx, item in enumerate(heights):
        if (idx == 0):
            answer.append(0)
        else:
            for checks in reversed(range(idx)):
                if heights[checks] > item:
                    note = checks + 1
                    break
                else:
                    note = 0
            answer.append(note)

    return answer

# 3번째 작성 , 정확도 87.5 / 100
def solution(heights):
    answer = []
    note = 0
    for idx, item in enumerate(heights):
        if (idx == 0):
            answer.append(0)
        else:
            for checks in reversed(range(idx)):
                if heights[checks] > item:
                    note = checks + 1
                    break
            answer.append(note)
    return answer

#2번째 작성 , 정확도 50 / 100
def sol2(heights):
    answer = []
    note = 0
    for idx, item in enumerate(heights):
        if (idx == 0):
            answer.append(0)
        else:
            for checks in reversed(range(idx)):
                if heights[checks] > item:
                    note = checks + 1
            answer.append(note)
    return answer

#1번째 작성 , 정확도 : 62 / 100
def sol1(heights):
    answer = []
    for idx, item in enumerate(heights):
        if(idx > 0): # idx == 1
            if(heights[idx - 1] > item):
                answer.append(idx)
            else:
                answer.append(0)
        else:
            answer.append(0)
            
    return answer

