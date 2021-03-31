N,K=map(int,input().split())

seq=[i for i in range(1,N+1)]
idx=0
answer=[]
while seq:
    idx=(idx+K-1)%len(seq)
    answer.append(str(seq.pop(idx)))
    
print("<"+", ".join(answer)+">")