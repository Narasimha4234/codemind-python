n=int(input())
ar=list(map(int,input().split()))
if(len(set(ar))==1):
    print(0)
else:
    c=mc=0
    for i in range(n):
        c=0
        for j in range(i,n):
            if(ar[i]==ar[j]):
                c+=1
                if(mc<c):
                    mc=c
    print(mc)