L, C = map(int, input().split())
alpha = list(input().split())
alpha = sorted(alpha)

# 모음
vowels = ['a', 'e', 'i', 'o', 'u']
# 자음
consonant = [chr(i) for i in range(97, 123) if chr(i) not in vowels ]

selected = []
def combinations(idx):
    if len(selected) >= L: 
        v_cnt = 0
        c_cnt = 0
        for s in selected:
            if s in vowels:
                v_cnt += 1
        
            else:
                c_cnt += 1
        if c_cnt >= 2 and v_cnt >=1:
            print(''.join(sorted(selected)))


        return

    for i in range(idx, C):
        selected.append(alpha[i])
        combinations(i+1)
        selected.pop()

combinations(0)