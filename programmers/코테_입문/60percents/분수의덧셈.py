def solution(numer1, denom1, numer2, denom2):
    answer = []

    if denom1 == denom2:
        answer.append(numer1 + numer2)
        answer.append(denom1)
        if answer[0] % answer[1] == 0:
            answer[0] = answer[0] // answer[1]
            answer[1] = 1
        else:
            answer_copy = answer.copy()
            while answer_copy[1]:
                answer_copy[0], answer_copy[1] = answer_copy[1], answer_copy[0] % answer_copy[1]
            if answer_copy[0] > answer[0]:
                answer[0] = answer_copy[0] // answer[0]
                answer[1] = answer_copy[0] // answer[1]
            else:
                answer[0] = answer[0] // answer_copy[0] 
                answer[1] = answer[1] // answer_copy[0] 

    else:
        answer.append(numer1 * denom2 + numer2 * denom1)
        answer.append(denom1 * denom2)
        if answer[0] % answer[1] == 0:
            answer[0] = answer[0] // answer[1]
            answer[1] = 1
        else:
            answer_copy = answer.copy()
            while answer_copy[1]:
                answer_copy[0], answer_copy[1] = answer_copy[1], answer_copy[0] % answer_copy[1]
            if answer_copy[0] > answer[0]:
                answer[0] = answer_copy[0] // answer[0]
                answer[1] = answer_copy[0] // answer[1]
            else:
                answer[0] = answer[0] // answer_copy[0] 
                answer[1] = answer[1] // answer_copy[0]

    return answer

print(solution(1,2,3,4))
print(solution(9,2,1,3))
print(solution(11,22,22,22))


# 두 숫자의 최대 공약수를 구하는 함수
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# print(gcd(33,22))