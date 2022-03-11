import heapq
test=int(input())
for i in range(test):
    arr,own=map(int,input().split())
    use=[int(x) for x in input().split()]
    give=[int(x) for x in input().split()]
    print(use)
    print(use)
    new=[]
    for i in range(len(use)):
        heapq.heappush(new,(use[i],give[i]))
    while new:
        ram,add=heapq.heappop(new)
        if ram<=own:
            own+=add
        else:
            break
    print(own)