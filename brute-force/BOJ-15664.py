def solution_1(N,M):
    selected=[]
    visited=[False]*N

    def combination(start,cnt):
        if cnt == M:
            for idx in range(N):
                if visited[idx]==True:
                    print(sortedList[idx],end=' ')
            # for element in selected:
            #     print(element,end=' ')
            print()
            return

        ##inputlist를 sorting 했기 때문에 바로 직전의 수와 현재 idx의 값이 다르기만 하면
        ##중복되지 않기 때문에 prev를 썼다.
        prev=-9999999999
        for i in range(start,N):    
            if visited[i] == False and prev!=sortedList[i]:
                visited[i]=True
                selected.append(sortedList[i])
                prev=sortedList[i]
                combination(i+1,cnt+1)
                
                visited[i]=False
                ##i번째 idx 다 돌고 재귀 스택 다 종료된 경우
                if cnt==0:
                    selected.clear()


    combination(0,0)

##dictionary 써서 str으로 조합을 이어 붙이고 기존의 조합이 없는 경우만 print...
def solution_2(N,M):
    selected=[]
    visited=[False]*N
    dict={}

    def combination(start,cnt):
        caseComb=""
        if cnt == M:
            for element in selected:           
                caseComb+=str(element)+' '
            if dict.get(caseComb)==None:
                dict[caseComb]=dict.get(caseComb,0)+1
                print(caseComb)

        for i in range(start,N):    
            selected.append(sortedList[i])
            combination(i+1,cnt+1)
                
            selected.pop()
                
    combination(0,0)


if __name__ == "__main__":
    N,M=map(int,input().split())
    inputList=list(map(int,input().split()))
    sortedList=sorted(inputList)
    solution_1(N,M) 
    print(2)
    solution_2(N,M)