import sys
M, N, L = map(int, sys.stdin.readline().split())
hunters = list(map(int, sys.stdin.readline().split()))
animals = []

for i in range(N):
    animals.append(list(map(int, sys.stdin.readline().split())))

hunters.sort()
animals.sort()

def dist_animal_to_hunter(hunter, animal):
    x = abs(hunter - animal[0])
    y = animal[1]
    return x + y


answer = 0
for animal in animals:
    start = 0
    end = M - 1
    while start <= end:
        mid = (start + end) // 2
        dist = dist_animal_to_hunter(hunters[mid], animal)

        if dist <= L:
            answer += 1
            break
        else:
            if hunters[mid] >= animal[0]:
                end = mid - 1
            else:
                start = mid + 1

print(answer)
