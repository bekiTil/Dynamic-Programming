import heapq
test=int(input())
for i in range(test):
    length=int(input())
    num=[int(x) for x in input().split()]
    num.sort()
    i=len(num)-1
    red=0
    while i>length//2:
        n=num.pop()
        red+=n
        i-=1
    if length%2==0:
        if red>sum(num[:-1]):
            print("Yes")
        else:
            print("No")
    else:
        if red>sum(num):
            print("Yes")
        else:
            print("No")