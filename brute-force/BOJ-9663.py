##문제를 잘못 이해했다. 가로 세로 대각선 한칸 즉 총 현 좌표에서 주변 8개의 좌표에만
##퀸이 없으면 되는 줄 알아서 아래와 같이 구현했다....
def solution_2(N):
    visited = [[False for _ in range(N)]for _ in range(N)]
    # noPath=[[False for _ in range(N)]for _ in range(N)]
    noPathList = [[] for _ in range(N)]
    # print(noPathList)
    dir = [[-1, 0], [-1, -1], [-1, 1], [0, 1],
           [0, -1], [1, 0], [1, -1], [1, 1]]
    caseCnt = []
    flag = 0

    def findNQueen(posX, posY, cnt):
        if cnt == N:
            caseCnt.append(cnt)
            print(caseCnt)
            return

        visited[posX][posY] = True
        # print(posX,posY,cnt)
        for dirX, dirY in dir:
            noPathX = posX+dirX
            noPathY = posY+dirY
            if noPathX < 0 or noPathY < 0 or noPathX >= N or noPathY >= N:
                continue
            # print(noPathX,noPathY)
            # noPath[noPathX][noPathY]=True
            noPathList[cnt].append((noPathX, noPathY))
            # print(noPathList)

        for i in range(posX, N):
            for j in range(posY, N):
                for x, y in noPathList[cnt]:
                    # print(x,y)
                    if x == i and y == j:
                        flag = 1
                        break
                    flag = 0

                if visited[i][j] == False and flag == 0:
                    findNQueen(i, j, cnt+1)
                    visited[i][j]=False
                    noPathList[cnt].clear()

        # findNQueen()

    findNQueen(0, 0, 1)
    print("여긱기기")
    print(len(caseCnt))

def solution_1(N):
    visited = [[False for _ in range(N)]for _ in range(N)]
    # noPath=[[False for _ in range(N)]for _ in range(N)]
    noPathList = [[] for _ in range(N)]
    # print(noPathList)
    dir = [[-1, 0], [-1, -1], [-1, 1], [0, 1],
           [0, -1], [1, 0], [1, -1], [1, 1]]
    caseCnt = []
    flag = 0

    def validPos(x,y):
        if x<0 or y<0 or x>=N or y>=N:
            return False
        return True

    def diagonal(noPathList,cnt,currentX,currentY):
        pDiagX=currentX
        pDiagY=currentY

        mDiagX=currentX
        mDiagY=currentY
        for i in range(N):
            mDiagX=mDiagX-i
            mDiagY=mDiagY+i
            if validPos(mDiagX,mDiagY):
                noPathList[cnt].append((mDiagX,mDiagY))

            pDiagX=pDiagX+i
            pDiagY=pDiagY-i
            if validPos(pDiagX,pDiagY):
                noPathList[cnt].append((pDiagX,pDiagY))

    def row(noPathList,cnt,currentX,currentY):
        pRowX=currentX
        pRowY=currentY

        mRowX=currentX
        mRowY=currentY

        for i in range(N):
            mRowX=mRowX-i
            if validPos(mRowX,mRowY):
                noPathList[cnt].append((mRowX,mRowY))

            pRowX=pRowX+i
            if validPos(pRowX,pRowY):
                noPathList[cnt].append((pRowX,pRowY))

    def col(noPathList,cnt,currentX,currentY):
        pColX=currentX
        pColY=currentY

        mColX=currentX
        mColY=currentY
        
        for i in range(N):
            mColY=mColY-i
            if validPos(mColX,mColY):
                noPathList[cnt].append((mColX,mColY))

            pColY=pColY+i
            if validPos(pColX,pColY):
                noPathList[cnt].append((pColX,pColY))
    
    def findNQueen(posX, posY, cnt):
        if cnt == N:
            caseCnt.append(cnt)
            return

        visited[posX][posY] = True
        diagonal(noPathList,cnt,posX,posY)
        row(noPathList,cnt,posX,posY)
        col(noPathList,cnt,posX,posY)
        print(noPathList)
        for i in range(posX, N):
            for j in range(posY, N):
                for x, y in noPathList[cnt]:
                    # print(x,y)
                    if x == i and y == j:
                        flag = 1
                        break
                    flag = 0

                if visited[i][j] == False and flag == 0:
                    findNQueen(i, j, cnt+1)
                    visited[i][j]=False
                    noPathList[cnt].clear()

        # # findNQueen()

    findNQueen(0, 0, 1)
    print("여긱기기")
    print(len(caseCnt))

import sys
sys.setrecursionlimit(10 ** 8)
def solution_3(N):
    visited = [[False for _ in range(N)]for _ in range(N)]

    def possible_path(x, y):
        if 0<=x<N and 0<=y<N:
            return True
    
        return False

    # 상하좌우 대각선 전 범위에서 이미 퀜이 존재하는지 확인
    def is_exist(x, y):
        # 상하좌우 체크
        for lr in visited[x]:
            if lr == True:
                return False
        
        for row in range(N):
           if visited[row][y] == True:
                return False
        
        # 대각선 위쪽 체크
        lu = ru = y
        for row in range(x-1, -1, -1):
            # 대각선 왼쪽 위
            lu -= 1
            if possible_path(row, lu) and visited[row][lu]:

                return False
            
            # 대각선 오른쪽 위
            ru += 1
            if possible_path(row, ru) and visited[row][ru]:
                return False
        

        # 대각선 아래쪽 체크
        lu = y
        ru = y
        for row in range(x+1, N, 1):
            # 대각선 왼쪽 아래
            lu -= -1
            if possible_path(row, lu) and visited[row][lu]:
                return False

            # 대각선 오른쪽 아래
            ru += 1
            if possible_path(row, ru) and visited[row][ru]:
                return False
        
        return True

    
    def dfs(x, y, queen_cnt):
        global answer
        if queen_cnt == N:
            answer += 1
            return
        
        for i in range(N):
            for j in range(N):
                if possible_path(i, j) and not visited[i][j]:
                    if not is_exist(i, j):
                        continue

                    visited[i][j] = True
                    dfs(i, j, queen_cnt+1)
                    visited[i][j] = False
                

    dfs(0,5,0)
    print(answer[0])

if __name__ == "__main__":
    N = int(input())
    # solution_2(N)
    # solution_1(N)
    answer = 0
    solution_3(N)

