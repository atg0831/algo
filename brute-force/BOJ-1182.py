import sys
# recursion depth 더 깊게 설정
sys.setrecursionlimit(10**7)

N, S = map(int, sys.stdin.readline().split())
numlist = list(map(int, sys.stdin.readline().split()))
selected = []


def my_combination(start):
    if selected and sum(selected) == S:
        global cnt
        cnt += 1
        # return
        # return 하면 안된다 왜냐하면 그 뒤의 숫자들이 -5,5 이런식으로 뒤이어지면 두개의 합은
        # 0이니까 이것도 부분수열에 포함해주어야 하므로...

    for i in range(start, N):
        selected.append(numlist[i])
        my_combination(i+1)
        selected.pop()


cnt = 0
my_combination(0)

print(cnt)
