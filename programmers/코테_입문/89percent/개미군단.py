def solution(hp):
    answer = 0
    while hp > 0:
        if hp // 5 > 0:
            answer += hp // 5
            hp -= 5 * (hp // 5)
        elif hp // 3 > 0 :
            answer += hp // 3
            hp -= 3 * (hp // 3)
        elif hp // 1 > 0:
            answer += hp // 1
            hp -= 1 * (hp // 1)
    return answer

print(solution(23))
print(solution(24))
print(solution(999))

#다른풀이
def solution(hp):    
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)