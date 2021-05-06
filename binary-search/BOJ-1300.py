N = int(input())
K =int(input())

start = 1
max_ = N * N
end = max_

length = N * N

mid_val = 0
while start <= end:
    mid = (start + end) // 2
    length //= 2
    if length % 2 == 0:
        length -= 1

    # mid_val =
    # if mid > K:
    #     end = mid - 1
    #     mid_val = mid_val - length
    # elif mid < K:
    #     start = mid + 1
    #     mid_val = mid_val + length

    # else:
    #     print(mid_val)
    #     break
