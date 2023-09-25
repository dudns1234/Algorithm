def solution(i, j, k):

    temp = [ str(i) for i in range(i,j+1) ]

    temp2 = ''.join(temp)

    return temp2.count(str(k))


print(solution(1,13,1))
print(solution(10,50,5))
print(solution(3,10,2))

# 다른 풀이
def solution(i, j, k):
    answer = sum([ str(i).count(str(k)) for i in range(i,j+1)])
    return answer
