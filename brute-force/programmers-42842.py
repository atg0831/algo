def solution(brown, yellow):
    answer = []
    total_size=brown+yellow
    # height,width는 최소 3보다 커야 되고 width의 첫 시작은 total/3부터 시작하여 1씩 작아지는데
    # total_size의 약수인지 판별하고 아니라면 패스...    
    for width in range(int(total_size/3),2,-1):
        if total_size%width>0:
            continue
        height=int(total_size/width)
        
        y_paint=(height-2)*(width-2)
        if y_paint==yellow:
            answer.append(width)
            answer.append(height)
            break
    return answer

