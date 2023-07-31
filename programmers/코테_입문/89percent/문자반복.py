def solution(my_string, n):
    answer = []
    for i in my_string:
        #print(i*n)
        answer.append(i*n)
    return ''.join(answer)

print(solution("hello",3))


# 다른 풀이
def solution(my_string, n):
    answer = ''
    for m in my_string:
        answer += (m * n)
    return answer
