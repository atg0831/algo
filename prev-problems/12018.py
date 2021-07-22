n,m=list(map(int,input().split()))
arr=[]
PL_arr=[]
arr_temp=[]
count=0
for i in range(0,n):
    P,L=(map(int,input().split()))
    PL_arr.append([P,L])
    arr.append(list(map(int,input().split())))

index=0
for i,j in PL_arr:
    if i>=j:
        arr[index].sort(reverse=True)
        arr_temp.append(arr[index][j-1])
    else:
        m-=1
        if(m>=0):
            count+=1
    index+=1

arr_temp.sort()
if m>0:
    for i in arr_temp:
        m-=i
        if m<0:
            break
        else :
            count+=1

print(count) 
