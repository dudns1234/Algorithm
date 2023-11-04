import math

def solution(n):
    sqrt = math.isqrt(n) 
    if sqrt * sqrt == n:  # 제곱수 맞는지 확인-> 왜? math.isqrt(9)=>3이며, math.isqrt(8)=>2로 나오기 때문에 제곱을 해서 맞는지 확인
        return 1
    else:
        return 2
    
print(solution(144))
print(solution(976))
print(solution(101))