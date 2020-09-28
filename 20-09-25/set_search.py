n = int(input())
narr = set(map(int, input().split()))

a = int(input())
aarr = list(map(int, input().split()))

for i in aarr:
    if i in narr:
        print("yes", end=" ")
    else:
        print("no", end=" ")