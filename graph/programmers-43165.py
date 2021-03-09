numbers = list(map(int, input().split()))
target = int(input())

length = len(numbers)
cnt = 0


def dfs(idx, factor, value):
    global cnt
    if idx >= length:
        if value == target:
            cnt += 1

        return

    # selected.append(numbers[idx]*factor)
    dfs(idx+1, factor, value+numbers[idx]*factor)
    factor *= -1
    dfs(idx+1, factor, value+numbers[idx]*factor)


def solution(numbers, target):
    answer = 0
    dfs(0, 1, 0)
    answer = cnt
    return answer


solution(numbers, target)
