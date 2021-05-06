def solution(number, k):
    answer = ''
    length=len(number)
    # 뒤에 남아있는 문자열 갯수
    left=length-k-1
    index=length-left

    #자른 구간의 리스트 값중 Max값 저장시키는 배열(최초값은 -1로 입력)
    index_max=[-1]
    i=1
    while index<=length :
        temp=number[index_max[i-1]+1:index]
        Max=max(temp)
        # 이전에 저장했던 Max 인덱스값 다음부터 Max값 조사 후 append(최대값이 같은게 여러개 있을경우 고려)
        index_max.append(number.index(Max,index_max[i-1]+1))
        k=k-(index_max[i]-index_max[i-1]-1)

        if k==0:
            answer=answer+number[index-1:]
            break       
                    
        answer=answer+Max  
        index+=1
        i+=1

    return answer

N,K=map(int,input().split())
number=(input())
print(solution(number,K))