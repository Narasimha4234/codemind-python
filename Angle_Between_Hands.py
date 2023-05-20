a,b=map(int,input().split(":"))
x=abs(30*a-((11/2)*b))
d=360-x
if x<d:
    print(x)
else:
    print(d)