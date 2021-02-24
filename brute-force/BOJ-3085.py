def cal_max_candy(candy, N):
    max_candy=0
    for row in range(N):
        row_cnt = []
        col_cnt = []
        queue = []
        for col in range(N):
            if not queue:
                queue.append((candy[row][col], candy[col][row]))
                row_cnt.append(1)
                col_cnt.append(1)
                max_candy=max(max_candy,1)
                continue

            row_prev, col_prev = queue.pop()
            if row_prev == candy[row][col]:
                current_cnt = row_cnt.pop()
                row_cnt.append(current_cnt+1)
                max_candy=max(max_candy,current_cnt+1)
            else:
                row_cnt.append(1)

            if col_prev == candy[col][row]:
                current_cnt = col_cnt.pop()
                col_cnt.append(current_cnt+1)
                max_candy=max(max_candy,current_cnt+1)
            else:
                col_cnt.append(1)

            queue.append((candy[row][col], candy[col][row]))
    return max_candy    

def swap_col(candy,row,col):
    candy[row][col],candy[row][col+1]=candy[row][col+1],candy[row][col]

def swap_row(candy,row,col):
    candy[row][col],candy[row+1][col]=candy[row+1][col],candy[row][col]

def solution(candy, N):
    answer=0
    for row in range(N):
        for col in range(N):
            if col<N-1:
                swap_col(candy,row,col)
                answer=max(answer,cal_max_candy(candy,N))
                swap_col(candy,row,col)
            
            if row<N-1:
                swap_row(candy,row,col)
                answer=max(answer,cal_max_candy(candy,N))
                swap_row(candy,row,col)
    
    print(answer)

# N = int(input())
# candy = []
# for i in range(N):
#     candy.append(input().split())
#     # candy[i] = list(map(str, input().split()))

# candy=[list(input().split()) for _ in range(N)]
from sys import stdin
N=int(stdin.readline())
candy = [list(stdin.readline().rstrip()) for _ in range(N)]
solution(candy, N)
