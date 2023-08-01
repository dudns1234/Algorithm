def solution(box, n):
    answer = 1
    for i in range(len(box)):
        answer *= box[i]
    return answer // n ** 3

print(solution([1, 1, 1], 1))
print(solution([10, 8, 6], 3))

# 다른 풀이
def solution(box, n):
    answer = 1
    for i in range(len(box)):
        answer *= (box[i]//n)
    return answer

def solution(box, n):
    answer = 1
    for b in box:
        answer *= b // n
    return answer