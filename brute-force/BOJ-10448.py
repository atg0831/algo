import itertools
def Tn(num):
    tri=[]
    for n in range(1,num):
        element=int((n*(n+1))/2)
        tri.append(element)
        if element>=num:
            return tri
    
    return (tri)

def solution_1(num):
    tri=Tn(1000)
    for i in itertools.product(tri,repeat=3):
        if sum(i)==num:
            print(1)
            return
    print(0)

def solution_2(num):
    tri=Tn(1000)
    for i in tri:
        for j in tri:
            for k in tri:
                if (i+j+k)==num:
                    print(1)
                    return
    
    print(0)

def solution_3(num):
    tri=Tn(1000)
    ##여기는 직접 재귀로 구현...
    ##문제는 재귀 종료 조건을 효율적으로 구현해야 됨
    
N=int(input())
inputlist=[]
for _ in range(N):
    element=int(input())
    solution_1(element)
    solution_2(element)
