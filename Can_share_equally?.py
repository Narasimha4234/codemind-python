a,b=map(int,input().split())
x=a*1
y=b*2
if a%2==0 and (a>0 or b%2==0):
    print("YES")
else:
    print("NO")