# just use list to create recursive combination function
def solution_1(N, M):
    inputList = [i for i in range(0, N+1)]
    selected = [False]*(N+1)

    def Combinations(start, cnt):
        if cnt == M:
            for i in range(1, N+1):
                if selected[i] == True:
                    print(inputList[i], end=' ')
            print()
            return
        for i in range(start, N+1):
            if selected[i] == True:
                continue

            selected[i] = True
            Combinations(i+1, cnt+1)
            selected[i] = False

    Combinations(1, 0)

# use stack to create recursive combination function(list.append()...)


def solution_2(N, M):
    inputList = [i for i in range(0, N+1)]
    selected = []

    def Combinations(start, cnt):
        # if len(selected)==M
        if cnt == M:
            for element in selected:
                print(element, end=' ')
            print()
            return
        for i in range(start, N+1):
            selected.append(inputList[i])
            # Plus one with last in element of selected
            # due to choose next element when Combinations called
            start = selected[-1]+1
            Combinations(start, cnt+1)
            selected.pop()

    Combinations(1, 0)

# not using iterative, but only recursive


def solution_3(N, M):
    inputList = [i for i in range(0, N+1)]
    selected = []

    def combinations(start):
        if len(selected) == M:
            for element in selected:
                print(element, end=' ')
            print()
            return

        # 더 이상 뽑을 조합이 없다 잘못된 조합을 추출하고 있었으니 return
        if start >= N+1:
            return

        # 이번 index 원소 뽑는 경우
        selected.append(inputList[start])
        combinations(start+1)

        # 이번 index의 값을 selected에서 빼고 index+1로 재귀 call...
        selected.pop()
        combinations(start+1)

    combinations(1)


if __name__ == "__main__":
    N, M = map(int, input().split())

    solution_1(N, M)
    print(2)
    solution_2(N, M)
    print(3)
    solution_3(N, M)
