T = int(input())

for _ in range(T):
    weights = []
    k, n = map(int, input().split())
    for _ in range(4):
        weights.append(list(map(int, input().split())))

    class1 = []
    class2 = []

    # i=0, i=2 두가지 경우([(weights[0], weights[1]), (weights[2], weights[3])])
    for i in range(0,4,2):
        for w in weights[i]:
            for _w in weights[i+1]:
                if i == 0:
                    class1.append(w+_w)
                else:
                    class2.append(w+_w)
    
    class1.sort()
    class2.sort()
    answer = -1
    temp = []
    for w in class1:
        left_weight = k - w
        total1 = 0
        total2 = 0
        diff1 = float('inf')
        diff2 = float('inf')
        start = 0
        end = len(class2) - 1

        while start <= end:
            mid = (start + end) //2

            if class2[mid] == left_weight:
                answer = k
                break

            elif class2[mid] > left_weight:
                end = mid -1
                total1 = class2[mid] + w
                diff1 = abs(k-total1)
                
            else:
                start = mid + 1
                total2 = w + class2[mid]
                diff2 = abs(k-total2)
            
        
        if answer == k:
            break
        
        
        if diff1 < diff2:
            temp.append([diff1,total1])    
        else:
            temp.append([diff2,total2])
        
    if len(temp) > 0:
        temp = sorted(temp, key=lambda x: (x[0], x[1]))
        answer = temp[0][1]

    print(answer)