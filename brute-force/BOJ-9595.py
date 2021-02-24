import sys
import itertools
sys.setrecursionlimit(10**7)


def use_itertools():
    global cnt
    # 각 permutaion은 (1)부터 ....(1,1,1,1,.....) num 갯수만큼 존재한다.
    for repeat_num in range(1, num+1):
        # 중복을 허락한 permutaion==prduct!
        for i in list(itertools.product(range(1, 4), repeat=repeat_num)):
            if sum(i) == num:
                cnt += 1



def use_my():
    selected = []
    numlist_of_permutation = [1, 2, 3]

    def my_repeted_permutaion():
        global cnt

        if sum(selected) == num:
            cnt += 1
            return

        if len(selected) >= num:
            return

        for i in range(3):
            selected.append(numlist_of_permutation[i])
            my_repeted_permutaion()

            selected.pop()

    my_repeted_permutaion()

def solution_1():
    use_itertools()
    print("itertools의 product 사용")


def solution_2():
    use_my()
    print("직접 repeated_permutaion 구현하여 사용")


test_case = int(input())
for _ in range(test_case):
    num = int(input())
    cnt = 0
    solution_1()
    print(cnt)
    cnt=0
    # my_repeted_permutaion()
    solution_2()
    print(cnt)
