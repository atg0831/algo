N,M=map(int,input().split())
location=list(map(int,input().split()))
location.append(0)
list_plus=[]
list_minus=[]
location.sort()
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
    if(minus_count<=M and plus_count<=M):
        if(comp>0):
            sum+=abs(list_minus[0])+2*list_plus[0]
        else :
            sum+=2*abs(list_minus[0])+list_plus[0]
           
    elif(minus_count>M and plus_count<=M):        
        count=minus_count-M
        index=minus_count-count
        if(comp>0):
            sum+=list_plus[0]*2+abs(list_minus[0])
        else:
            sum+=list_plus[0]+2*abs(list_minus[0])
        while 1 :
            if(count>M):
                arr.append(list_minus[index:index+M])
                count=count-M
                index=minus_count-count
            else:
                arr.append(list_minus[index:minus_count])
                for i in arr:
                    sum+=abs(i[0])*2
                break

    elif(minus_count<=M and plus_count>M):
        count=plus_count-M
        index=plus_count-count
        if(comp>0):
            sum+=abs(list_minus[0])+2*list_plus[0]
        else :
            sum+=2*abs(list_minus[0])+list_plus[0]
          
        while 1 :
            if(count>M):
                arr.append(list_plus[index:index+M])
                count=count-M
                index=plus_count-count
            else:
                arr.append(list_plus[index:plus_count])
                for i in arr:
                    sum+=(i[0])*2
                break

    elif(minus_count>M and plus_count>M):
        count1=minus_count-M
        count2=plus_count-M
        index1=minus_count-count1
        index2=plus_count-count2
        if(comp>0):
            sum+=abs(list_minus[0])+2*list_plus[0]
        else:
            sum+=2*abs(list_minus[0])+list_plus[0]

        while 1 :
            if(count1>M):
                arr.append(list_minus[index1:index1+M])
                count1=count1-M
                index1=minus_count-count1
            else :
                arr.append(list_minus[index1:minus_count])
                for i in arr:
                    sum+=abs(i[0])*2
                break
        while 1 :
            if(count2>M):
                arr2.append(list_plus[index2:index2+M])
                count2=count2-M
                index2=plus_count-count2
            else :
                arr2.append(list_plus[index2:plus_count])
                for i in arr2:
                    sum+=(i[0])*2
                break
            
print(sum)

