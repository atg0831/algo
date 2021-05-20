N = int(input())
words = []

for _ in range(N):
    words.append(str(input()))

alpha_dict = {}

for word in words:
    length = len(word)
    for i in range(length):
        alpha_dict[word[i]] = alpha_dict.get(word[i], 0) + 10**(length-1)
        length -= 1

alpha_list = sorted(alpha_dict.items(), key=lambda x: x[1], reverse=True)
number = [i for i in range(9, -1, -1)]
answer = 0
i = 0
for _, value in alpha_list:
    answer += value * number[i]
    i += 1

print(answer)
