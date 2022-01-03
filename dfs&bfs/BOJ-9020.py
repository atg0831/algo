import math
T = int(input())
for _ in range(T):
    n = int(input())

    def is_prime(num):
        half = int(math.sqrt(num))
        if num == 1:
            return False
        if num == 2:
            return True
        for i in range(2, half+1):
            # if i % 2 == 0:
            #     continue

            if num % i == 0:
                return False
            
        return True
    a = [False,False] + [True]*(n-1)
    primes=[]
 
    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
    # primes = []
    # for i in range(1, n):
    #     if i != 2 and i % 2 == 0:
    #         continue
    #     if is_prime(i):
    #         primes.append(i)


    answer = []
    for p in range(len(primes)):
        sum_ = 0
        for q in range(p, len(primes)):
            sum_ = primes[p] + primes[q]
            sub = primes[q] - primes[p]
            if sum_ == n:
                if answer:
                    if sub < (answer[0][1] - answer[0][0]):
                        answer.pop()
                        answer.append((primes[p],primes[q]))
                
                else:
                    answer.append((primes[p],primes[q]))
    
    print(answer[0][0], end = ' ')
    print(answer[0][1])

# for aa in a:
#     print(aa[0][0], end = ' ')
#     print(aa[0][1])

    # answer_list = []
    # for i in range(1, n):
    #     sum_ = 0
    #     for j in range(i, n):
    #         sum_ = i + j
    #         if sum_ == n:
    #             if is_prime(i) and is_prime(j):
    #                 if answer_list:
    #                     if (answer_list[0][1] - answer_list[0][0]) > (j-i):
    #                         answer_list.pop()
    #                         answer_list.append((i, j))
    #                 else:
    #                     answer_list.append((i, j))

    # print(*answer_list, sep=' ')
    # print(answer_list[0][0], end = ' ')
    # print(answer_list[0][1])
