def solution(sides):
    answers = 0
    sides.sort()
    for i in range(len(sides)-1):
        answers += sides[i]
    if max(sides) >= answers:
        return 2
    else:
        return 1
    
print(solution([1, 2, 3]))
print(solution([3, 6, 2]))
print(solution([199, 72, 222]))

# 다른 방법(코테에서는 오답으로 나오는데 답들은 다 맞음)
def solution(sides):
    answer = 0
    for i in sides:
        if i != max(sides):
            answer += i
    if max(sides) >= answer:
        return 2
    else:
        return 1
    
print(solution([1, 2, 3]))
print(solution([3, 6, 2]))
print(solution([199, 72, 222]))

