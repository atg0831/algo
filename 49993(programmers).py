def solution(skill, skill_trees):
    answer = len(skill_trees)

    length_skill=len(skill)

    for element in skill_trees:
        len_element=len(element)
        stack=[]
        i=0
    
        for ch in element:
            # if i==length_skill:
            #     break
            for s in skill:
                if ch==s:
                    stack.append(ch)
                    i+=1
                    break
        
        stack_len=len(stack)
        j=0
        for context in stack:
            if context!=skill[j]:
                answer-=1
                break
            j+=1
                
#         index=element.find(skill[0])
#         stack=[]
#         if index==-1:
#             answer-=1
#             continue
#         else:
#             # if length_skill==1:
#             #     answer+=1
#             #     continue
                
#             stack.append([index,skill[0]])
#             i=1
#             while i<=length_skill-1:
#                 index=element.find(skill[i])
#                 if index!=-1:
#                     stack.append([index,skill[i]])
#                 i+=1
        
#         stack_len=len(stack)
#         stack.sort()
#         # print(stack)
#         if stack_len !=0:
#             for i in range(stack_len):
#                 # print(skill[i],stack[i][1])
#                 if skill[i]!=stack[i][1]:
#                     # print(element,answer,stack[i],i)
#                     answer-=1
#                     break
#                 # elif skill[i]==stack[i][1] and i==stack_len-1:
#                 #     print(element,answer,stack[i],i)
#                     # answer+=1
#                 # print(element,answer,stack[i],stack[i+1])

#                 # if stack[i]>stack[i+1]:
#                 #     break
#                 # elif stack[i]<stack[i+1] and i==stack_len-2:
#                 #     answer+=1

                

    return answer