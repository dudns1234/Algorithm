def solution(n, t):
    for i in range(1,t+1):
         n = n*2
    return n
    

print(solution(2,10))
print(solution(7,15))

# 다른풀이
def solution(n, t):
    answer = 2**t * n
    return answer

def solution(n, t):
    return n << t  # 비트시프트