def solution(balls, share):
    answer = 1
    answer2 = 1
    answer3 = 1
    a = (balls-share)

    for i in range(1,a+1):
        answer *= i

    for j in range(1,share+1):
        answer2 *= j

    for m in range(1,balls+1):
        answer3 *= m

    return answer3 // (answer * answer2)


print(solution(3,2))
print(solution(5,3))

# 다른 사람 풀이

import math

def solution(balls, share):
    return math.comb(balls, share)

