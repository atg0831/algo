def solution_1(N, M):
    selected = []

    def repeatedPermutation(cnt):
        if cnt == M:
            for element in selected:
                print(element, end=' ')
            print()
            return

        for i in range(0, N):
            selected.append(sortedList[i])
            repeatedPermutation(cnt+1)

            selected.pop()

    repeatedPermutation(0)


if __name__ == "__main__":
    N, M = map(int, input().split())
    inputList = list(map(int, input().split()))
    sortedList = sorted(inputList)
    solution_1(N, M)
