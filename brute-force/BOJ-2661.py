from itertools import product
N = int(input())
s_1 = []
s_2 = []
num = [1, 2, 3]
print(N)
for s in  list(product(range(1,4), repeat = 7)):
    print(s, end = ' ')
