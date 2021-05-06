N = int(input())
liquids = list(map(int, input().split()))
liquids = sorted(liquids)

start = 0
end = N - 1
answer = liquids[start] + liquids[end]
posx = start
posy = end

# start <= end 하면 안됨 같은 값을 더하는 경우는 존재하지 않으므로
while start < end:
    sum_ = liquids[start] + liquids[end]
    if abs(sum_) < abs(answer):
        answer = sum_
        posx = start
        posy = end
        if answer == 0:
            break

    if sum_ < 0:
        start += 1
    else:
        end -= 1

print(liquids[posx], liquids[posy])


    

