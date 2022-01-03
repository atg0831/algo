n = int(input())
convenient_name = list(input())
signs = [input()for _ in range(n)]
answer = 0
for sign in signs:
    same_cnt = 0
    flag = False
    for i, s in enumerate(sign):
        if s == convenient_name[0]:
            for gap in range(1, 19):
                same_cnt = 1
                iter = 0
                if flag:
                    break
                for j in range(i+gap, len(sign), gap):
                    iter += 1
                    if sign[j] == convenient_name[same_cnt]:
                        same_cnt += 1

                    if iter == len(convenient_name)-1:
                        if same_cnt == len(convenient_name):
                            flag = True
                            break
                        break
                    # if same_cnt == len(convenient_name):
                    #     flag = True
                    #     break
                same_cnt = 0
            break
        # if flag:
            # break

    if flag:
        answer += 1
print(answer)