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