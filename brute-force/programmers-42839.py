from itertools import permutations
import math
def solution(numbers):
    answer = 0
    prime=[]
    
    def is_prime(number):
        if number==1 or number!=2 and number%2==0:
            return False
        else:
            for i in range(2,int(math.sqrt(number))+1):
                if number%i==0:
                    return False
        
        return True
    
    
    for repeat in range(1,len(numbers)+1):
        number=list(map(''.join,permutations(numbers,repeat)))
        number=set(number)
        for num in number:
            if is_prime(int(num)):
                prime.append(int(num))
    
    prime=set(prime)
    answer=len(prime)
    return answer