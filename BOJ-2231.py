import math

def solution(N):

    def extract_each_num(num):
        return num%10

    def cal_decomposite_sum(iter,M):
        total_sum=M
        temp=M
        for i in range(iter):
            each=extract_each_num(temp)
            total_sum+=each
            ## '//' 연산자 쓰면 (num-num)/10 이렇게 할 필요 없이 (num)//10
            # tempM=((tempM-each)/10)
            temp=temp//10
            if temp<1:
                break

        return total_sum

    n_size=len(N)
    if n_size==1:
        return 0

    for M in range(int(math.pow(10.0,(n_size-2))),int(N)):
        decom_sum=cal_decomposite_sum(n_size,M)
        if int(decom_sum)==int(N):
            return M

    return 0

N=str(input())
M=solution(N)
print(M)