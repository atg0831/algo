def solution1():
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

def solution2():
    l, c = map(int, input().split())
    char = list(map(str, input().split()))

    vowels = ['a', 'e', 'i', 'o', 'u']
    consonant = [chr(i)for i in range(97, 123) if chr(i) not in vowels]


    char.sort()
    def my_combination(idx, encryption, n):
        if len(encryption) == l:
            vowels_cnt = consonant_cnt = 0
            for e in encryption:
                if e in vowels:
                    vowels_cnt += 1
                else:
                    consonant_cnt += 1
            if vowels_cnt >= 1 and consonant_cnt>=2:
                print(encryption)

            return
        

        for i in range(idx, n):
            my_combination(i+1, encryption + char[i], n)
            
    my_combination(0,"", c)

if __name__ == "__main__":
    print("solution1")
    solution1()
    
    print("solution2")
    solution2()