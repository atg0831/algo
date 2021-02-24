from sys import stdin


def paint(chess):
    color = ["B", "W"]
    total_cnt = []
    # 첫번째 요소가 B이거나 W 두가지 경우로 나누고 더 적은 paint 갯수를 return
    for case in range(2):
        cnt = 0
        for i in range(8):
            temp = list(chess[i])
            # case==0 이면 B먼저 시작하고 그러면 다음 row는 W로 시작해야된다.
            # case==1 이면 W먼저 시작하고 다음 row는 B로 시작하는 등 지그재그로 color선택
            prev = color[(case+i) % 2]
            for current in temp:
                if prev == current:
                    B, W = color
                    if current == B:
                        current = W
                    else:
                        current = B
                    cnt += 1
                prev = current
        total_cnt.append(cnt)
    return min(total_cnt)


def sliceboard(i, j, board):
    chess = []
    chess.append([row[0][j:j+8] for row in board[i:i+8]])
    paint_cnt = paint(chess[0])
    return paint_cnt


def solution(N, M, board):
    minimum = 30000
    for start in range(N-7):
        for end in range(M-7):
            paint_cnt = sliceboard(start, end, board)
            if minimum > paint_cnt:
                minimum = paint_cnt

    return minimum


N, M = list(map(int, input().split()))
# board=[list(stdin.readline().rstrip()) for _ in range(N)]
board = [list(input().split()) for _ in range(N)]
print(solution(N, M, board))
