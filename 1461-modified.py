# 수정본
def cal(count,index,list,arr,sum,location_count):
    while 1 :
        if(count>M):
            arr.append(list[index:index+M])
            count=count-M
            index=location_count-count
        else:
            arr.append(list[index:location_count])
            for i in arr:
                sum+=abs(i[0])*2
            break
    return sum

N,M=map(int,input().split())
location=list(map(int,input().split()))
location.append(0)
location.sort()
list_plus=[]
list_minus=[]

index=location.index(0)
if index==N:
    list_plus.append(0)
else :
    list_plus=location[index+1:N+1]
list_minus=location[0:index]
minus_count=len(list_minus)
plus_count=len(list_plus)
if minus_count==0:
    list_minus.append(-0)
list_plus.sort(reverse=True)
comp=abs(list_minus[0])-list_plus[0]
sum=0

if M==1:
    if(comp>0):
        last_index=0
    else : 
        last_index=N
    sum=abs(location.pop(last_index))
    
    for i in location:
        sum=sum+abs(i*2)

else :
    arr=[]
    arr2=[]
    if(comp>0):
            sum+=abs(list_minus[0])+2*list_plus[0]
    else :
            sum+=2*abs(list_minus[0])+list_plus[0]
 
    if(minus_count>M and plus_count<=M):        
        count=minus_count-M
        index=minus_count-count
        sum=cal(count,index,list_minus,arr,sum,minus_count)
     
    elif(minus_count<=M and plus_count>M):
        count=plus_count-M
        index=plus_count-count
        sum=cal(count,index,list_plus,arr,sum,plus_count)

    elif(minus_count>M and plus_count>M):
        count1=minus_count-M
        count2=plus_count-M
        index1=minus_count-count1
        index2=plus_count-count2
        sum=cal(count1,index1,list_minus,arr,sum,minus_count)
        sum=cal(count2,index2,list_plus,arr2,sum,plus_count)
            

print(sum)