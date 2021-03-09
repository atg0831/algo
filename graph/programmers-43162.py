def solution(n, computers):
    answer = 0
    visited = [False]*n

    def dfs(vertex):
        if vertex >= n:
            return
        visited[vertex] = True

        for i in range(n):
            if computers[vertex][i] == 1 and visited[i] == False:
                dfs(i)

    for i in range(n):
        if visited[i] == False:
            dfs(i)
            answer += 1

    return answer
  

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n,computers))