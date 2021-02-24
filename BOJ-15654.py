def solution(N, M):
    selected = []

    def permutation(cnt):
        if cnt == M:
            for element in selected:
                print(element, end=' ')
            print()
            return

        for i in range(0, N):
            if sortedList[i] not in selected:
                selected.append(sortedList[i])
                permutation(cnt+1)
                selected.pop()

    permutation(0)


if __name__ == "__main__":
    N, M = map(int, input().split())
    inputList = list(map(int, input().split()))
    sortedList = sorted(inputList)
    solution(N, M)
