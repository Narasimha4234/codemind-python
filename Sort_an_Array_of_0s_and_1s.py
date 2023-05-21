a=int(input())
li=list(map(int,input().split()))
li.sort()
for i in li:
    print(int(i),end=" ")
    