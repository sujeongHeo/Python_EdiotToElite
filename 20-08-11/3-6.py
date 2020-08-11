n, k = map(int, input().split())
result = 0 
while True:
    # (N == K 로 나누어 떨어지는 수) 가 될 때 까지 1씩 빼기
    target = (n //k ) * k
    result += result - target
    n = target 
    #  N 이 K 보다 작으면 ???
    if n < k:
        break
    result += 1
    n //= k