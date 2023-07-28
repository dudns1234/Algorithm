def solution(money):
    answer = []
    answer.append(int(money / 5500))
    answer.append(int(money - (int(money / 5500) * 5500 )))
    
    return answer

print(solution(5500))
print(solution(15000))