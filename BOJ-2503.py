cnt = 0


def decomposenum(num):
    each = []
    for _ in range(3):
        each.append(num % 10)
        num = num//10
    return each


def validate(num):
    for i in range(3):
        if num[i] == 0:
            return False

    if num[0] == num[1] or num[0] == num[2] or num[1] == num[2]:
        return False

    return True

def det_strike_or_ball(eachinfo,eachnum):
    strike=0
    ball=0
    for i in range(3):
        if eachinfo[i]==eachnum[i]:
            strike+=1
        elif eachinfo[i] in eachnum:
            ball+=1
    return (strike,ball)

def solution_1(N, info):
    global cnt
    for i in range(123, 988):
        eachnum = decomposenum(i)
        ##숫자가 0이 들어가거나 각 자리수 중 중복이 있으면 다음 숫자로 넘어간다.(이거 안해주면 정답이 틀릴 수도 있다.)
        if not validate(eachnum):
            continue

        checkcnt = 0
        for j in range(N):
            eachinfo = decomposenum(info[j][0])
            # if eachinfo[0] == eachnum[0]:
            #     strike += 1
            # if eachinfo[0] == eachnum[1] or eachinfo[0] == eachnum[2]:
            #     ball += 1
            # if eachinfo[1] == eachnum[1]:
            #     strike += 1
            # if eachinfo[1] == eachnum[0] or eachinfo[1] == eachnum[2]:
            #     ball += 1
            # if eachinfo[2] == eachnum[2]:
            #     strike += 1
            # if eachinfo[2] == eachnum[0] or eachinfo[2] == eachnum[1]:
            #     ball += 1

            strike,ball=det_strike_or_ball(eachinfo,eachnum)
            if strike == info[j][1] and ball == info[j][2]:
                checkcnt += 1

        # 모든 질문에 대한 s,b이 성립하는지 체크하기 위함
        if checkcnt == N:
            cnt += 1

    print(cnt)

import itertools
def solution_2(N,info):
    global cnt
    for i in itertools.permutations(range(1,10),3):
        # eachnum=decomposenum(i)
        eachnum=[]
        ##itertools.permutaion의 결과는 tuple(1,2,3)이렇게 나온다 
        ##위의 solution_1 구현한다고 eachnum,eachinfo를 리스트로 구현해서 아래처럼 구현 
        eachnum.append(i[2])
        eachnum.append(i[1])
        eachnum.append(i[0])      
        checkcnt=0
        for j in range(N):
            eachinfo=decomposenum(info[j][0])
            strike,ball=det_strike_or_ball(eachinfo,eachnum)
            if strike == info[j][1] and ball == info[j][2]:
                checkcnt += 1
        
        if checkcnt==N:
            cnt+=1

    print(cnt)

N = int(input())
info = []
for _ in range(N):
    info.append(list(map(int, input().split())))

solution_1(N, info)
cnt=0
solution_2(N,info)
