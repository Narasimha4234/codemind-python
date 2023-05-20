a=int(input())
for i in range(a):
    c=0
    y=int(input())
    n=list(map(int,input().split()))
    x=len(n)
    for j in range(x):
        if(n[j]%2!=0):
            c+=1
    print(c//2)