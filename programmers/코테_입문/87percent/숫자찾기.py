def solution(num, k):

    if str(k) in list(str(num)):
        return list(str(num)).index(str(k))+1
    else:
        return -1
        
            

    


print(solution(29183,1))
print(solution(232443,4))
print(solution(123456,7))

