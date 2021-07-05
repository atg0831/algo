def solution(name):
    answer = 0
    print(ord('Z')- ord('A'))
    
    def distance_alpha(from_, to_):
        return abs(ord(from_) - ord(to_))
    
    def left_or_right(idx, name):
        left_dist =0 
        right_dist = 0
        last = 0
        for i in range(idx-1, idx, -1):
            left_dist += 1
            if name[i] != 'A':
                last = i
                break
        
        for j in range(idx+1, len(name)):
            right_dist += 1
            if name[j] != 'A':
                last = j
                break
        
        if left_dist > right_dist:
            return (last, right_dist, False, 1)
        else:
            return (last, left_dist, False, -1)
        
            
    cursor = 0
    flag = True
    factor = 1
    temp = ['A' for _ in range(len(name))]
    print(temp)
    while 1:
        dist = distance_alpha("A", name[cursor])
        if dist >= 13:
            answer += 26 - dist
        elif dist < 13:
            answer += dist
        
        temp[cursor] = name[cursor]
        cursor += factor * 1
        if name[cursor] == "A" and flag:
            cursor, d, flag, factor = left_or_right(cursor, name)
            answer += d

        temp_str = ''.join(temp)
        print(temp_str)
        if ''.join(temp) == name:
            break
        answer += 1
            
    return answer

print(solution("JAN"))   