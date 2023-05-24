n=int(input())
li=list(map(int,input().split()))
gcd=li[0]
i=0
j=1
while j<n:
    if li[j]%gcd==0:
        j+=1
    else:
        gcd=li[j]%gcd
        i+=1
print(gcd)
