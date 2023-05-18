n=input()

while(len(n)>1):
    sum=0
    for i in range(len(n)):
        sum=sum+int(n[i]);
    n=str(sum)
print(n)