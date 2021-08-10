n = int(input())

y = list(map(int, input().split()))
x = [i for i in range(n)]

scopes = [[0 for _ in range(n)]for _ in range(n)]

def cal_scope(x1, x2, y1, y2):
    if x1!=x2:
        scope = (y1-y2)/(x1-x2)
    
    return scope

see_list = [[0 for _ in range(n)]for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        scope = cal_scope(i, j, y[i], y[j])
        scopes[i][j] = scopes[j][i] = scope
        # see_list[i][j] = see_list[j][i] = 1
        # 여기서 본인 바로 옆의 건물은 무조건 보일거니까 see_cnt=1로 시작
        see_cnt = 1
        # 본인 바로 옆 건물 빼고 그 다음 건물부터 체크
        for k in range(i+1, j):
            if scopes[i][k] < scopes[i][j]:
                see_cnt = 1
            else:
                see_cnt = 0
                break
        # 바로 옆 건물은 무조건 see_cnt = 1이고 나머지는 위 반복문에서 see_cnt 결정된 것으로 see_list에 대입
        see_list[i][j] = see_list[j][i] = see_cnt

        
max_ = 0        
for see in see_list:
    cnt = sum(see)
    if max_ < cnt:
        max_ = cnt

print(max_)