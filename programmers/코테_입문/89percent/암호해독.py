def solution(cipher, code):
    answer = ''
    for i in range(1,len(cipher)+1):
        if int(i) % code == 0:
            answer += cipher[int(i)-1]
        else:
            pass

    return answer

print(solution("dfjardstddetckdaccccdegk",4))
print(solution("pfqallllabwaoclk",2))

# 다른 풀이 
def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer