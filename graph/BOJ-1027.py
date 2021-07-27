N = int(input())

xs = [i for i in range(N)]
ys = list(map(int, input().split()))

buildings = []
for x, y in zip(xs, ys):
    buildings.append([x, y])


# scopes, buildings_cnt 모두 두 선분으로 이루어져 있는 빌딩이므로 [i][j], [j][i] 값은 항상 같아야한다
scopes = [[0 for _ in range(N)] for _ in range(N)]
buildings_cnt = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        x_sub = buildings[i][0] - buildings[j][0]
        y_sub = buildings[i][1] - buildings[j][1]
        if x_sub != 0:
            scope = y_sub / x_sub
        else:
            scope = 0
        
        # 기울기는 [i][j] = [j][i] 
        scopes[i][j] = scopes[j][i] = scope

        
        # 바로 옆 건물이면 무조건 볼 수 있으므로 우선 1을 더함
        buildings_cnt[i][j] = buildings_cnt[j][i] = 1
        
            # 만약 i빌딩에서 j번 위치를 볼 때 i빌딩에서 각각 i+1에서 j-1번 빌딩의 기울기가 더 크다면
            # i번에서 j 빌딩 선분으로 그엇을 때 겹치는 부분이 생기므로 cnt를 0으로 한다.
        for k in range(i+1, j):
            if scopes[i][k] >= scopes[i][j]:
                buildings_cnt[i][j] = buildings_cnt[j][i] = 0
                break

answer = 0
for building in buildings_cnt:
    cnt = sum(building)
    if answer < cnt:
        answer = cnt

print(answer)
                
                

