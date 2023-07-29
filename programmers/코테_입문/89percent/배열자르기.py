def solution(numbers, num1, num2):
    answer = numbers[num1:num2+1]
    return answer

print(solution([1, 2, 3, 4, 5],1,3))
print(solution([1, 3, 5],1,2))


# 다른풀이
def solution(numbers, num1, num2):
    answer = []
    for i in numbers[num1:num2+1]:
        answer.append(i)

    return answer

def solution(numbers, num1, num2):
    answer=[]
    for i in range(num1,num2+1):
        answer.append(numbers[i])
    return answer