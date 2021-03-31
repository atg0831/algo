p = [int(input()) for _ in range(9)]
visited = [False for _ in range(9)]
selected = []


def my_combination(idx, cnt, sum_):
    if cnt == 7:
        if sum_ == 100:
            for element in sorted(selected):
                print(element)
            exit()
        return

    for i in range(idx, 9):
        if not visited[i]:
            visited[i] = True
            selected.append(p[i])
            my_combination(i+1, cnt+1, sum_+p[i])
            visited[i] = False
            selected.pop()


my_combination(0, 0, 0)
