answer = 0


def solution(begin, target, words):
    # answer = 0
    def one_diff(begin, word):
        cnt = 0
        for i in range(len(begin)):
            if begin[i] == word[i]:
                cnt += 1

        if cnt == len(target)-1:
            return True
        else:
            return False

    min_list = []
    min_cnt = 0
    visited = [False]*len(words)
    selected = []

    def dfs(temp_begin, words, target, cnt):
        global answer
        if temp_begin == target:
            answer = cnt
            return

        for i in range(len(words)):
            if visited[i] == True:
                continue

            if one_diff(temp_begin, words[i]):
                # selected.append(words[i])
                visited[i] = True

                temp_begin = words[i]
                dfs(temp_begin, words, target, cnt+1)
                # selected.pop()
                # visited[i]=False
                # temp_begin=selected[-1]

    dfs(begin, words, target, 0)
    print(answer)
    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))
