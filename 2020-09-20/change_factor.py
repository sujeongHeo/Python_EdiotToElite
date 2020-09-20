n, k = map(int, input().split()) # N 과 K 를 입력받기
a = list(map(int, input().split())) # 배열 A 의 모든 원소를 입력 받기
b = list(map(int, input().split())) # 배열  B 의 모든 원소를 입력 받기 

a.sort() # 배열A 는 오름차순 정렬 수행 
b.sort(reverse = True) # 배열 B는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며 , 두 배열의 원소를 최대 K번 비교
for i in range(k):
    #A의 원소가 B의 원소보다 작은 경우
    if(a[i] < b[i]):
        # 두 원소 교체
        a[i] , b[i] = b[i], a[i]
    else:
        break
print(sum(a))