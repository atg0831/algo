from sys import stdin
from collections import deque


while True:
    lines = stdin.readline().rstrip()
    if lines == ".":
        break
    
    stack = deque()
    for line in lines:
        if line == "(" or line == "[":
            stack.append(line)

        elif line == ")" or line == "]":
            if len(stack) == 0:
                stack.append("no")
                break

            top = stack[-1]
            if line == ")":
                if top == "(":
                    stack.pop()
                # [인 경우
                else:
                    stack.append("no")
                    break

            elif line == "]":
                if top == "[":
                    stack.pop()
                # (인 경우
                else:
                    stack.append("no")
                    break

    if len(stack) == 0:
        print("yes")
    else:
        print("no")
