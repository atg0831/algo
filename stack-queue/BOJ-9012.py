from sys import stdin

T=int(input())

for test_case in range(T):
    brackets=list(map(str,stdin.readline().rstrip()))
    stack=[]
    for bracket in brackets:
        if bracket!=")":
            stack.append(bracket)
            continue

        if len(stack)==0:
            stack.append(")")
            break
        prev=stack.pop()

    
    if len(stack)==0:
        print("YES")
    else:
        print("NO")