def solution(n):
    answer = 0
    for i in range(n+1):
        if int(i) % 2 == 0:
            answer += int(i)
    return answer

print(solution(10))
print(solution(4))
