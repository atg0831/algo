N = int(input())
sign = list(map(str, input().split()))
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# permutaion 느낌
selected = []
ans = []


def recur(sign_cnt):
    if len(selected) == N+1:
        temp = ""
        for element in selected:
            temp = temp+element
        ans.append(temp)
        return

    for idx in range(10):
        if selected == []:
            selected.append(number[idx])
            recur(sign_cnt)

        else:
            if number[idx] in selected:
                continue

            if sign[sign_cnt] == "<":
                if selected[-1] < number[idx]:
                    selected.append(number[idx])
                    recur(sign_cnt+1)
                else:
                    continue

            else:
                if selected[-1] > number[idx]:
                    selected.append(number[idx])
                    recur(sign_cnt+1)
                else:
                    continue

        selected.pop()


recur(0)

ans.sort()
print(ans[-1])
print(ans[0])
