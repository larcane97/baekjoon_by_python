n = int(input())
lope=[]
for _ in range(n):
    lope.append(int(input()))
lope.sort(reverse=True)
ret= lope[0]
for i in range(1,n):
    ret = max(ret,(i+1)*lope[i])
print(ret)
    
