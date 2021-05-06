# Counter로 같은 나무 높이 개수 미리 구하면 시간 단축 가능
N, M = map(int, input().split())
trees = list(map(int, input().split()))

highest = max(trees)
start = 1
end = highest - 1
answer = 0

while start <= end:
    mid = (start + end) // 2
    
    cut_len = 0
    for tree in trees:
        if tree-mid <= 0:
            continue
        if cut_len >= M:
            break
        cut_len += (tree - mid)

    if cut_len >= M:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
        

print(answer)


