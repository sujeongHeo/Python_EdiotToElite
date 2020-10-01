# 떡 갯수 , 요청한 떡의 길이
n, m = list(map(int, input().split(' ')))

# 각 떡 개별 높이 정보
array = list(map(int, input().split()))

# 이진 탐색 위한 시작점, 끝점 
start = 0 
end = max(array)

result = 0
while (start <= end):
    total = 0
    mid = (start + end ) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < m :
            end = mid -1
    else :
        result = mid
        start = mid + 1

print(result)