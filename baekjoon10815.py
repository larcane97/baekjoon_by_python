n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
a.sort()
answer=[False]*m
for i in range(len(b)):
    left,right=0,len(a)-1
    while left<=right:
        mid=(left+right)//2
        if a[mid]<b[i]:
            left=mid+1
        elif a[mid]>b[i]:
            right=mid-1
        else:
            answer[i]=True
            break
for i in answer:
    if i: print(1,end=' ')
    else: print(0,end=' ')
