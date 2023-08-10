# 공배수 찾기 문제
def solution(n):
    answer = []
    answer2 = []
    for i in range(1,101):
        answer.append(n * i)
        answer2.append(6*i)
    
    for i in answer:
        if i in answer2:
            return answer2.index(i)+1
        

print(solution(6))
print(solution(10))
print(solution(4))

# 다른 풀이
def solution(n):
    i=1
    while(1):
        if (6*i)%n==0:
            return i
        i+=1
