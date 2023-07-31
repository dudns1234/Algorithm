def solution(num_list):
    return num_list[::-1]

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 1, 1, 1, 1, 2]))
print(solution([1, 0, 1, 1, 1, 3, 5]))


# 다른풀이
def solution(num_list):
    answer = []
    
    num_list.reverse()
    answer = num_list
    
    return answer

def solution(num_list):
    answer = []
    
    for num in num_list:
        answer.insert(0, num)

    return answer
