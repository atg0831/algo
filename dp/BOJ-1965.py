n = int(input())
box_size = list(map(int, input().split()))

in_box = [0 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if box_size[i] > box_size[j]:
            in_box[i] = max(in_box[i], in_box[j] + 1 ) 

print(max(in_box[n-1]) + 1) 