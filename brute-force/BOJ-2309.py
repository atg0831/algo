from itertools import combinations

def solution_1(p):
    answer=[]
    comb_list=list(combinations(p,7))
    for list_value in comb_list:
        partial_sum=sum(list_value)
        if partial_sum==100:
            sorted_list=sorted(list_value)
            answer=(sorted_list)
            return answer
    # print(combList)

def solution_2(p):
    answer=[]
    visited=[False for _ in range(9)]
    def my_combination(start,cnt):
        if cnt==7:
            if sum(answer)==100:
                sorted_answer=sorted(answer)
                for element in sorted_answer:
                    print(element)
                exit()

            return

        for idx in range(start,9):
            if visited[idx]==True:
                continue
            visited[idx]=True
            answer.append(p[idx])
            my_combination(start+1,cnt+1)
            visited[idx]=False
            answer.pop()

    my_combination(0,0)

def solution_3(p):
    answer=[]
    def my_combination(start,cnt):
        if cnt==7:
            if sum(answer)==100:
                sorted_answer=sorted(answer)
                for element in sorted_answer:
                    print(element)
                # exit()  ##문제에서 정답이 여러가지가 존재할 수 있다고 했으므로 print하고 난 뒤에 다른 경우의 정답을 출력하지 않기 위해서 exit
            
            return

        if start>=9:
            return

        answer.append(p[start])
        my_combination(start+1,cnt+1)

        answer.pop()
        my_combination(start+1,cnt)

    my_combination(0,0)

if __name__ == "__main__":
    p=[[] for _ in range(9)]
    for i in range(9):
        p[i]=int(input())

    answer=solution_1(p)
    for i in range(7):
        print(answer[i])

    print("----2----")
    solution_2(p)

    print("---3-----")
    solution_3(p)
    