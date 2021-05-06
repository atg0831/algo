import sys
N=int(sys.stdin.readline())
letter=list(map(str,sys.stdin.readline()))
letter.pop(-1)

letter2=sorted(letter,key=lambda x : x[0])
def choice(letter,letter2,N):
    answer1=""
    answer2=""
    
    for _ in range(N):
        str1=letter.pop(-1)
        answer1=answer1+str1
        letter2.remove(str1)
        str2=letter2.pop(0)
        letter.remove(str2)
        answer2=answer2+str2

    if(answer2<answer1):
        return "DA",answer2
    else :
        return  "NE",answer2
        
a,b=choice(letter,letter2,int(N/2))
print(a)
print(b)